import hashlib
import requests

def hash_pom_content_blake2b(url):
    """
    Generate a Blake2b hash of the content of a .pom file fetched from a URL.

    Args:
    - url (str): The URL of the .pom file.

    Returns:
    - str: The hexadecimal representation of the Blake2b hash of the content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error

        blake2b_hash = hashlib.blake2b()
        blake2b_hash.update(response.content)
        
        return blake2b_hash.hexdigest()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL '{url}': {e}")
        return None

# Example usage:
url = "https://repo1.maven.org/maven2/hivemind/hivemind/1.0-rc-2/hivemind-1.0-rc-2.pom"
hash_value = hash_pom_content_blake2b(url)
if hash_value:
    print(f"Blake2b hash of content from {url}: {hash_value}")
