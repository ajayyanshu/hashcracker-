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
```
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
```
### 2. Dictionary Attack (-d)
Tests every word from a given wordlist file (e.g., rockyou.txt).

```bash
# Example: Crack a password using a wordlist
# Hash for 'password' (md5): e10adc3949ba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
python3 cracker.py e10adc3949ba59abbe56e057f20f883e \
    -a md5 \
    -d /path/to/rockyou.txt
```
### 3. Rule-Based Attack (-d + -r)
The most powerful attack. Applies a set of common mutations to every word in your dictionary.

```bash
# Example: Crack 'Password123' using the base word 'password'
# Hash for 'Password123' (sha1): c254b5505372b86f488583457016312b84781d05
python3 cracker.py c254b5505372b86f488583457016312b84781d05 \
    -a sha1 \
    -d /path/to/rockyou.txt \
    -r
```
### 4. Mask Attack
A highly-targeted brute-force. Use this when you know parts of the password.

Mask Syntax:

• ?l = Lowercase letter (a-z)

• ?u = Uppercase letter (A-Z)

• ?d = Digit (0-9)

• ?s = Special Symbol (!@#$%...)

• Any other character is a literal.

```bash
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
```
---
### ❤️ Support & Donations
If you find this tool helpful and want to support itIf you find HashCrackPro useful and would like to support its development, please consider making a donation. Your contributions help us maintain and improve the project.

[![Donate](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjd9o3K2CK9LObsNOok8nY4WYMSwKkhAzsz7NDxmO8eZU-d8dw4kEKW1Ycp3QpzVsT2okmWwoBXLXB757yQhoL0Xandlt3Wjwdw7tTlU4hTGdJcFH1tq1i0K6o7uTTGK-20fKi7DQhgoYEZkHI1-Y9UPBWAjiNhtn8TceqHS4O6kTaaeNweZe6OBJ0Ve0ou/s424/download.png)](https://buymeacoffee.com/ajayyanshu)

[![Donate](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMgW12teTME3e1Ap4Lc6MuQ7mFoEfyKINWAQ8dDx0vRR6XXNXGNXSaOgFdFhB2kTv8d6r5TiMIpRqJv9EnrM2YU1Syrvq4KO32YcmjiJk-GLuxHGMwfTPIO1Zz1JE2lCSMTRcrY1JJues1jpC4qotBNumo3d3dC79uRFulGasM8vzSdneJmzunxKDiUKI2/s386/upi.PNG)]()
s development, please consider donating. Every little bit helps!


---
## Contact with us

For inquiries and support, please contact us at [ajayyanshu@gmail.com](mailto:ajayyanshu@gmail.com).

----

## Contributions

Contributions are welcome! Please fork this repository and submit pull requests with your enhancements.
----

⚠️ Disclaimer

This tool is intended for educational purposes, cybersecurity training (CTFs), and authorized security audits only. The developer is not responsible for any malicious or illegal use of this software.
