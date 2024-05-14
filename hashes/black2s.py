import pyblake2

def hash_jar_file_blake2s(file_path):
    """
    Generate a hash of a jar file using Blake2s algorithm.

    Args:
    - file_path (str): Path to the jar file.

    Returns:
    - str: The hexadecimal representation of the hash.
    """
    try:
        with open(file_path, "rb") as file:
            hash_object = pyblake2.blake2s()
            for chunk in iter(lambda: file.read(4096), b""):
                hash_object.update(chunk)
            return hash_object.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage:
file_path = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\hivemind-1.0-rc-2.jar"
hash_value = hash_jar_file_blake2s(file_path)
if hash_value:
    print(f"Hash of {file_path}: {hash_value}")
