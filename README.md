# HTTP-Request-Smuggling

Disclaimer
This tool is for educational purposes only. Ensure you have explicit permission before testing any system. Unauthorized use is illegal.

# SPYDIRBYTE: HTTP Request Smuggling Tool

SPYDIRBYTE is an ethical hacking tool designed to detect HTTP Request Smuggling vulnerabilities in web servers.

## Features
- Test for CL.TE (Content-Length vs. Transfer-Encoding) vulnerabilities.
- Test for TE.CL (Transfer-Encoding vs. Content-Length) vulnerabilities.
- Simple to use and customizable.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SPYDIRBYTE.git
   cd SPYDIRBYTE

2. Install dependencies:
pip install requests

Usage
Run SPYDIRBYTE with Python 3.x:
python spydirbyte.py -u <target_url> -t <test_type>

Replace <target_url> with the URL you want to test.
Replace <test_type> with:
cl.te for Content-Length vs. Transfer-Encoding.
te.cl for Transfer-Encoding vs. Content-Length.
all to run both tests.

Example:
python spydirbyte.py -u http://example.com -t all
