# 🔒 Phishing URL Detector

A simple Python script that helps identify potentially malicious or phishing URLs using a set of basic heuristics and a list of known phishing domains.

## 📌 Features

- Detects if a URL belongs to a known phishing domain
- Warns if the URL:
  - Does not use HTTPS
  - Contains suspicious keywords (like `login`, `verify`, etc.)
  - Returns an unexpected status code
  - Is unreachable

## 📁 File Structure

- `intern.py` — Main script to run phishing checks on user-provided URLs

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed. You'll also need the following packages:

```bash
pip install requests beautifulsoup4
```

### Run the Script

```bash
python intern.py
```

Then enter a URL when prompted. The script will run several checks and let you know if it might be suspicious.

## 📋 Example

```bash
🔍 Scanning for Suspicious Links...
Enter a URL to check: http://malicious-site.com
The URL 'http://malicious-site.com' is potentially a phishing link.
```

## 🛡️ How it Works

- Parses the domain from the URL and compares it to a list of known phishing domains
- Checks for the presence of HTTPS
- Searches for suspicious keywords in the URL
- Tries to send an HTTP GET request to verify reachability

## 📝 Notes

- The list of phishing domains is just a placeholder. For real-world use, integrate with an up-to-date phishing domain feed or API.
- This tool is intended for **educational** or **basic internal use** only and should not be used as a sole line of defense against phishing.

## 📄 License

MIT License — free to use, modify, and distribute.
