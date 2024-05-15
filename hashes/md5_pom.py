

import hashlib
import requests

def hash_pom_content_md5(url):
    """
    Generate an MD5 hash of the content of a .pom file fetched from a URL.

    Args:
    - url (str): The URL of the .pom file.

    Returns:
    - str: The hexadecimal representation of the MD5 hash of the content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error

        md5_hash = hashlib.md5()
        md5_hash.update(response.content)
        
        return md5_hash.hexdigest()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL '{url}': {e}")
        return None

# Example usage:
url = "https://repo1.maven.org/maven2/hivemind/hivemind/1.0-rc-2/hivemind-1.0-rc-2.pom"
hash_value = hash_pom_content_md5(url)
if hash_value:
    print(f"MD5 hash of content from {url}: {hash_value}")
