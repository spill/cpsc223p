# Write a Python program that takes a URL as input and checks if the URL is valid or not. If the URL is valid, it prints "URL is valid" and extracts the scheme, netloc, path, parameters from it. If the URL is invalid, it catches the URLError exception and prints the error message.

 

# Hint: Try using modules URLError & urlparse

from urllib.parse import urlparse

def validate_url(url):
    try:
        result = urlparse(url)
        if not result.scheme or not result.netloc:
            print("URL is invalid.")
        else:
            print("URL is valid.")
            print("Scheme:", result.scheme)
            print("Netloc:", result.netloc)
            print("Path:", result.path)
            print("Parameters:", result.params)
    except ValueError as e:
        # Handle exceptions related to parsing issues
        print(f"URL is invalid: {str(e)}")

# Example usage
url_input = input("Please enter a URL to validate: ")
validate_url(url_input)
