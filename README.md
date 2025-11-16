### 1. Brute-Force Attack (`-b`)

Checks all combinations of a given charset up to a max length.

```bash
# Example: Crack a 5-character, all-lowercase password
# Hash for 'hello' (sha256): 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
python3 cracker.py 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 \
    -a sha256 \
    -b \
    -c abcdefghijklmnopqrstuvwxyz \
    -l 5
2. Dictionary Attack (-d)
Tests every word from a given wordlist file (e.g., rockyou.txt).

Bash

# Example: Crack a password using a wordlist
# Hash for 'password' (md5): e10adc3949ba59abbe56e057f20f883e
python3 cracker.py e10adc3949ba59abbe56e057f20f883e \
    -a md5 \
    -d /path/to/rockyou.txt
3. Rule-Based Attack (-d + -r)
The most powerful attack. Applies a set of common mutations to every word in your dictionary.

Bash

# Example: Crack 'Password123' using the base word 'password'
# Hash for 'Password123' (sha1): c254b5505372b86f488583457016312b84781d05
python3 cracker.py c254b5505372b86f488583457016312b84781d05 \
    -a sha1 \
    -d /path/to/rockyou.txt \
    -r
4. Mask Attack (-m)
A highly-targeted brute-force. Use this when you know parts of the password.

Mask Syntax:

?l = Lowercase letter (a-z)

?u = Uppercase letter (A-Z)

?d = Digit (0-9)

?s = Special Symbol (!@#$%...)

Any other character is a literal.

Bash

# Example: Crack a password like 'User2024'
# We guess the mask is: '?u?l?l?l?d?d?d?d'
# Hash for 'User2024' (md5): 98da995a6d3f20c438f2f6902e86663f
python3 cracker.py 98da995a6d3f20c438f2f6902e86663f \
    -a md5 \
    -m '?u?l?l?l?d?d?d?d'

# Example: Crack a password like 'Admin!23'
# We guess the mask is: 'Admin?s?d?d'
python3 cracker.py <hash_here> \
    -a sha256 \
    -m 'Admin?s?d?d'
❤️ Support & Donations
If you find this tool helpful and want to support its development, please consider donating. Every little bit helps!

☕ Buy Me a Coffee

GitHub Sponsors: Sponsor @your-username

BTC: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

ETH: 0x0000000000000000000000000000000000000000
