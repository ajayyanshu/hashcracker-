#!/usr/bin/env python3

import hashlib
import itertools
import sys
import argparse
import multiprocessing
import functools
import os # <-- New import
from tqdm import tqdm # <-- New import for progress bar

def hash_string(algorithm, text):
    """Hashes a string using the specified algorithm."""
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == 'sha3_256':
        return hashlib.sha3_256(text.encode()).hexdigest()
    else:
        raise ValueError('Unsupported algorithm.')

# --- WORKER FOR BRUTE-FORCE ---
def brute_force_worker(length, target_hash, algorithm, charset):
    """Worker for brute-force: checks all combos for one length."""
    for attempt in itertools.product(charset, repeat=length):
        attempt_text = ''.join(attempt)
        attempt_hash = hash_string(algorithm, attempt_text)
        if attempt_hash == target_hash:
            return attempt_text  # Found it!
    return None  # Found nothing at this length

# --- WORKER FOR DICTIONARY ---
def dictionary_worker(word, target_hash, algorithm):
    """Worker for dictionary: checks one word."""
    word = word.strip() # Clean up any newline characters
    attempt_hash = hash_string(algorithm, word)
    if attempt_hash == target_hash:
        return word  # Found it!
    return None # Not a match

def get_line_count(filepath):
    """Utility to count lines in a file for the progress bar."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for i, _ in enumerate(f):
                pass
        return i + 1
    except FileNotFoundError:
        print(f"[!] Error: Dictionary file not found at {filepath}")
        sys.exit(1)

# --- MAIN EXECUTION ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="A high-performance, multi-threaded hash cracking tool.",
        epilog="Brute-Force Example: python3 %(prog)s <hash> -a sha256 -b -c abc123 -l 6\n"
               "Dictionary Example: python3 %(prog)s <hash> -a sha256 -d rockyou.txt",
        formatter_class=argparse.RawTextHelpFormatter # Allows newlines in help
    )
    
    parser.add_argument("hash", help="The target hash to crack.")
    parser.add_argument("-a", "--algorithm", help="Hashing algorithm (md5, sha1, etc.)", required=True)

    # --- UPDATE: Mutually Exclusive Attack Modes ---
    # The user must pick EITHER brute-force OR dictionary, not both.
    attack_group = parser.add_mutually_exclusive_group(required=True)
    attack_group.add_argument("-b", "--bruteforce", action='store_true', help="Enable brute-force attack mode. Requires -c and -l.")
    attack_group.add_argument("-d", "--dictionary", help="Enable dictionary attack mode. Provide path to wordlist.")

    # Brute-force specific arguments
    parser.add_argument("-c", "--charset", help="Character set for brute-force (e.g., 'abc123')")
    parser.add_argument("-l", "--max_length", type=int, help="Maximum password length for brute-force.")

    args = parser.parse_args()
    args.algorithm = args.algorithm.lower()
    
    cpu_count = multiprocessing.cpu_count()
    found_password = None

    try:
        # --- BRUTE-FORCE ATTACK LOGIC ---
        if args.bruteforce:
            if not args.charset or not args.max_length:
                parser.error("Brute-force mode (-b) requires --charset (-c) and --max_length (-l).")
            
            print(f"--- Starting BRUTE-FORCE attack with {cpu_count} CPU cores ---")
            print(f"Target Hash: {args.hash} ({args.algorithm})")
            print(f"Charset: {args.charset} | Max Length: {args.max_length}")

            lengths_to_check = range(1, args.max_length + 1)
            
            worker_func = functools.partial(
                brute_force_worker, 
                target_hash=args.hash, 
                algorithm=args.algorithm, 
                charset=args.charset
            )
            
            with multiprocessing.Pool(processes=cpu_count) as pool:
                # Use imap_unordered for efficiency and to find the first result fast
                # We wrap this in tqdm to get a progress bar!
                results_iterator = pool.imap_unordered(worker_func, lengths_to_check)
                
                pbar = tqdm(total=args.max_length, desc="Checking Lengths", unit="len")
                for result in results_iterator:
                    pbar.update(1) # Update progress for each length finished
                    if result:
                        found_password = result
                        pool.terminate() # Stop all other workers
                        break
                pbar.close()

        # --- DICTIONARY ATTACK LOGIC ---
        elif args.dictionary:
            print(f"--- Starting DICTIONARY attack with {cpu_count} CPU cores ---")
            print(f"Target Hash: {args.hash} ({args.algorithm})")
            print(f"Wordlist: {args.dictionary}")
            
            line_count = get_line_count(args.dictionary)
            print(f"Total words to check: {line_count:,}")

            worker_func = functools.partial(
                dictionary_worker, 
                target_hash=args.hash, 
                algorithm=args.algorithm
            )
            
            with open(args.dictionary, 'r', encoding='utf-8', errors='ignore') as f, \
                 multiprocessing.Pool(processes=cpu_count) as pool:
                
                # imap_unordered is perfect. It passes one line at a time to the workers.
                # We wrap this in tqdm, tell it the total lines, and it just works!
                # chunksize tells the pool to send work in batches of 5000, which is much
                # more efficient than one line at a time.
                chunksize = 5000 
                pbar = tqdm(total=line_count, desc="Cracking", unit="words")
                for result in pool.imap_unordered(worker_func, f, chunksize=chunksize):
                    pbar.update(1) # Update for every word processed
                    if result:
                        found_password = result
                        pool.terminate() # Stop all other workers
                        break
                pbar.close()

    except KeyboardInterrupt:
        print("\n[!] Cracking stopped by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] An error occurred: {e}")
        sys.exit(1)

    # --- FINAL RESULT ---
    print("--- Attack finished ---")
    if found_password:
        print(f"\n[+] SUCCESS! Match found: {found_password}")
    else:
        print("\n[-] FAILED. No match found.")
