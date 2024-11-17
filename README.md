SPYDIRBYTE: HTTP Request Smuggling Tool
Disclaimer
This tool is for educational purposes only. Ensure you have explicit permission before testing any system. Unauthorized use is illegal and may result in severe consequences. Always adhere to ethical hacking guidelines.

About SPYDIRBYTE
SPYDIRBYTE is an ethical hacking tool designed to detect HTTP Request Smuggling vulnerabilities in web servers. These vulnerabilities can occur due to misconfigurations in how web servers handle HTTP headers, potentially allowing attackers to bypass security controls or hijack user sessions.

Features
Detect CL.TE (Content-Length vs. Transfer-Encoding) vulnerabilities.
Detect TE.CL (Transfer-Encoding vs. Content-Length) vulnerabilities.
Simple and customizable, designed for both beginners and professionals.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/SPYDIRBYTE.git
cd SPYDIRBYTE
Install dependencies:

bash
Copy code
pip install requests
Usage
Run SPYDIRBYTE with Python 3.x:

bash
Copy code
python spydirbyte.py -u <target_url> -t <test_type>
Options:
Replace <target_url> with the URL of the web server you want to test.
Replace <test_type> with:
cl.te for Content-Length vs. Transfer-Encoding tests.
te.cl for Transfer-Encoding vs. Content-Length tests.
all to run both tests.
Example:
To test for both vulnerabilities:

bash
Copy code
python spydirbyte.py -u http://example.com -t all
Output
SPYDIRBYTE will display information about:

HTTP response codes and response lengths.
Alerts if a potential vulnerability is detected.
Notes
CL.TE Vulnerability: Occurs when the server prioritizes the Content-Length header over the Transfer-Encoding header.
TE.CL Vulnerability: Occurs when the server prioritizes the Transfer-Encoding header over the Content-Length header.
License
This project is licensed under the MIT License.

Contributions
Feel free to contribute to SPYDIRBYTE! Submit pull requests for bug fixes or new features.

