
import hashlib

def hash_file(file_path):
    """
    Generate hashes of a file using multiple hash algorithms.

    Args:
    - file_path (str): Path to the file.

    Returns:
    - dict: A dictionary containing various hash values of the file.
    """
    try:
        all_hashes = {}
        with open(file_path, "rb") as file:
            sha1_hash = hashlib.sha1()
            sha256_hash = hashlib.sha256()
            md5_hash = hashlib.md5()
            blake2b_hash = hashlib.blake2b(digest_size=32)
            while True:
                data = file.read(65536)  # Read file in chunks of 64KB
                if not data:
                    break
                sha1_hash.update(data)
                sha256_hash.update(data)
                md5_hash.update(data)
                blake2b_hash.update(data)
            all_hashes['sha1 hash'] = sha1_hash.hexdigest()
            all_hashes['sha256 hash'] = sha256_hash.hexdigest()
            all_hashes['md5 hash'] = md5_hash.hexdigest()
            all_hashes['blake2b-256 hash'] = blake2b_hash.hexdigest()
        return all_hashes
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\Django-1.10rc1-py2.py3-none-any.whl"
hash_value = hash_file(file_path)
if hash_value:
    for key, val in hash_value.items():
        print(f"\n{key} : {val}")
print("")
