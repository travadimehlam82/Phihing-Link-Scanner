import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# List of known phishing domains (this is just a sample, you should use a more comprehensive list)
known_phishing_domains = [
    "example-phishing.com",
    "malicious-site.com",
    "phishing-example.org"
]

def is_phishing_domain(url):
    """Check if the domain is in the known phishing domains list."""
    domain = urlparse(url).netloc
    return domain in known_phishing_domains

def check_url(url):
    """Check the URL for phishing characteristics."""
    # Check if the domain is known for phishing
    if is_phishing_domain(url):
        return True

    # Check for HTTPS
    if not url.startswith("https://"):
        print(f"Warning: {url} does not use HTTPS.")
        # Instead of returning True, you might want to log this and continue checking
        # return True

    # Check for suspicious keywords in the URL
    suspicious_keywords = ["login", "secure", "account", "update", "verify"]
    if any(keyword in url for keyword in suspicious_keywords):
        print(f"Warning: {url} contains suspicious keywords.")
        # Instead of returning True, you might want to log this and continue checking
        # return True

    # Check if the URL is reachable
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"Warning: {url} returned status code {response.status_code}.")
            # Instead of returning True, you might want to log this and continue checking
            # return True
    except requests.exceptions.RequestException as e:
        print(f"Warning: Could not reach {url}. Error: {e}")
        return True

    # If none of the checks indicate phishing, return False
    return False

def main():
    print("🔍 Scanning for Suspicious Links...")
    url = input("Enter a URL to check: ")

    if check_url(url):
        print(f"The URL '{url}' is potentially a phishing link.")
    else:
        print(f"The URL '{url}' appears to be safe.")

if __name__ == "__main__":
    main()