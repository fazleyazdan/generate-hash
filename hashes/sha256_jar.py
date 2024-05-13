import hashlib

def hash_jar_file_sha256(file_path):
    """
    Generate a SHA-256 hash of a JAR file.

    Args:
    - file_path (str): Path to the JAR file.

    Returns:
    - str: The hexadecimal representation of the SHA-256 hash.
    """
    try:
        with open(file_path, "rb") as file:
            sha256_hash = hashlib.sha256()
            while True:
                data = file.read(65536)  # Read file in chunks of 64KB
                if not data:
                    break
                sha256_hash.update(data)
            return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\data\hivemind-1.0-rc-2.jar"
hash_value = hash_jar_file_sha256(file_path)
if hash_value:
    print(f"SHA-256 hash of {file_path}: {hash_value}")
