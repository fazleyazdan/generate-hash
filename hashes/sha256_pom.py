import hashlib
import requests

def hash_pom_content_sha256(url):
    """
    Generate a SHA-256 hash of the content of a .pom file fetched from a URL.

    Args:
    - url (str): The URL of the .pom file.

    Returns:
    - str: The hexadecimal representation of the SHA-256 hash of the content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error

        sha256_hash = hashlib.sha256()
        sha256_hash.update(response.content)
        
        return sha256_hash.hexdigest()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL '{url}': {e}")
        return None

# Example usage:
url = r"C:\Users\Fazle Yazdan\Desktop\My_projects\generate_hash\test_data\hivemind-1.0-rc-2.jar"
hash_value = hash_pom_content_sha256(url)
if hash_value:
    print(f"SHA-256 hash of content from {url}: {hash_value}")
