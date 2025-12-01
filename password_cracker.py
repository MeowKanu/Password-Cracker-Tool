import hashlib
import itertools
import string
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm


# Generate passwords using itertools
def generate_passwords(chars, min_length, max_length):
    for length in range(min_length, max_length + 1):
        for pwd in itertools.product(chars, repeat=length):
            yield ''.join(pwd)


# Hash checker
def check_hash(password, target_hash, hash_type):
    try:
        hash_fn = getattr(hashlib, hash_type)
    except AttributeError:
        return False

    hashed = hash_fn(password.encode()).hexdigest()
    return hashed == target_hash


# Crack using wordlist or brute-force
def crack_hash(target_hash, hash_type, wordlist=None, min_length=1, max_length=4, threads=20):
    if wordlist:
        try:
            with open(wordlist, "r") as file:
                passwords = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("[-] Wordlist file not found!")
            return
    else:
        passwords = generate_passwords(string.ascii_letters + string.digits, min_length, max_length)

    print("\n[+] Cracking password... Please wait.\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(check_hash, pwd, target_hash, hash_type): pwd for pwd in passwords}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Progress"):
            if future.result():
                password = futures[future]
                print(f"\n[+] Password found: {password}")
                return password

    print("\n[-] Password not found.")
    return None


def main():
    parser = argparse.ArgumentParser(description="Password Cracker Tool")

    parser.add_argument("hash", help="Target hash to crack")
    parser.add_argument("-t", "--type", default="md5", help="Hash type (md5, sha1, sha256...)")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file")
    parser.add_argument("--min_length", type=int, default=1, help="Minimum password length for brute force")
    parser.add_argument("--max_length", type=int, default=4, help="Maximum password length for brute force")
    parser.add_argument("--threads", type=int, default=20, help="Number of threads")

    args = parser.parse_args()

    crack_hash(
        target_hash=args.hash,
        hash_type=args.type,
        wordlist=args.wordlist,
        min_length=args.min_length,
        max_length=args.max_length,
        threads=args.threads
    )


if __name__ == "__main__":
    main()
