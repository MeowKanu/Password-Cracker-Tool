# Password Cracker Tool

A multithreaded Python-based password cracking tool that cracks hashed passwords using either a wordlist or brute-force password generation. Supports multiple hash types, progress tracking, and high-speed parallel execution.

## Features

- Crack hashes using dictionary (wordlist) attack
- Crack using brute-force password generation
- Supports MD5, SHA1, SHA256, SHA512, etc.
- Multithreading for fast cracking
- Progress bars using tqdm
- Brute-force customizable with min/max length
- Clean command-line interface (argparse)

## Project Structure

password-cracker/
│── password_cracker.py
│── wordlist.txt (optional)
└── README.md

shell
Copy code

## Installation

Install the required module:

pip install tqdm

shell
Copy code

## Usage

### Crack using a wordlist
python password_cracker.py <hash> -w wordlist.txt

shell
Copy code

### Brute-force mode
python password_cracker.py <hash> --min_length 1 --max_length 4

shell
Copy code

### Specify hash type
python password_cracker.py <hash> -t sha256 -w wordlist.txt

shell
Copy code

## Example

python password_cracker.py 098f6bcd4621d373cade4e832627b4f6 -w wordlist.txt

markdown
Copy code

This hash represents `"test"`.

## How It Works

1. Takes a target hash (MD5/SHA/etc.)
2. Loads passwords:
   - From a wordlist, OR  
   - Generates all combinations via itertools  
3. Hashes each password and compares with the target
4. Uses ThreadPoolExecutor for speed
5. Shows cracking progress with tqdm
6. Prints found password (if any)

## Requirements

- Python 3.8 or higher
- tqdm library

## Notes

- Brute-force with large max_length can take a long time
- Use small lengths for testing (1–4)
- Dictionary attacks are faster than brute-force

## License

MIT License
