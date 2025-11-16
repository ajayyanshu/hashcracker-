# PyHashCracker ⚡

**PyHashCracker** is a high-performance, multi-threaded password recovery tool written in Python. It is inspired by features from professional tools like Hashcat, but built to be a clean, modern, and extensible Python project.

This tool is for educational purposes and ethical, authorized use only.

---

## 🚀 Features

* **⚡ Multi-Threaded:** Uses all available CPU cores (`multiprocessing`) to dramatically speed up cracking.
* **🎯 Multiple Attack Modes:**
    * **Brute-Force:** Standard character-by-character attack.
    * **Dictionary:** Tests millions of words from a wordlist.
    * **Rule-Based:** Smartly mutates dictionary words (`pass` -> `Pass!`, `P@ss123`, etc.) to find common patterns.
    * **Mask Attack:** Targeted brute-force for known patterns (e.g., `Admin?d?d?d`).
* **📊 Live Progress Bar:** A clean, real-time progress bar for all attack modes using `tqdm`.
* **⚙️ Professional CLI:** A user-friendly command-line interface built with Python's `argparse` module, complete with help menus.

---

## 🛠️ Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/pyhashcracker.git](https://github.com/your-username/pyhashcracker.git)
    cd pyhashcracker
    ```

2.  Create a `requirements.txt` file with the following content:
    ```
    tqdm
    ```

3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

---

## 📖 Usage

The script is run from the command line, with your target hash as the first argument. You must then choose one attack mode.

### 💬 Get Help

To see all available commands and options, use the `-h` flag:
```bash
python3 cracker.py -h
---

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
