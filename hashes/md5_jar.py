import hashlib

def hash_jar_file_md5(file_path):
    """
    Generate an MD5 hash of a JAR file.

    Args:
    - file_path (str): Path to the JAR file.

    Returns:
    - str: The hexadecimal representation of the MD5 hash.
    """
    try:
        with open(file_path, "rb") as file:
            md5_hash = hashlib.md5()
            while True:
                data = file.read(65536)  # Read file in chunks of 64KB
                if not data:
                    break
                md5_hash.update(data)
            return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\hivemind-1.0-rc-2.jar"
hash_value = hash_jar_file_md5(file_path)
if hash_value:
    print(f"MD5 hash of {file_path}: {hash_value}")
