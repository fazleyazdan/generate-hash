import hashlib

def hash_jar_file(file_path):
    """
    Generate a hash of a jar file using Blake2b algorithm.

    Args:
    - file_path (str): Path to the jar file.

    Returns:
    - str: The hexadecimal representation of the hash.
    """
    try:
        with open(file_path, "rb") as file:
            hash_object = hashlib.blake2b(digest_size=32)
            for chunk in iter(lambda: file.read(4096), b""):
                hash_object.update(chunk)
            return hash_object.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\Django-1.1.3.tar.gz"
hash_value = hash_jar_file(file_path)
if hash_value:
    print(f"Hash of {file_path}: {hash_value}")
