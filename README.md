# SPYDIRBYTE HTTP Request Smuggling Tool

SPYDIRBYTE is a lightweight and effective Python tool designed to test for HTTP Request Smuggling vulnerabilities. It helps security researchers and penetration testers identify potential Content-Length vs. Transfer-Encoding (`CL.TE`) and Transfer-Encoding vs. Content-Length (`TE.CL`) vulnerabilities in web applications.

## Features

- **CL.TE Smuggling Detection**: Identifies potential Content-Length vs. Transfer-Encoding smuggling vulnerabilities.
- **TE.CL Smuggling Detection**: Identifies potential Transfer-Encoding vs. Content-Length smuggling vulnerabilities.
- **Multiple Test Modes**: Perform targeted or comprehensive tests for better accuracy.

## Requirements

- Python 3.7+
- `requests` library

You can install the required library using pip:

```bash
pip install requests
```
Usage
```bash
python spydirbyte.py -u <target_url> -t <test_type>
```

Arguments
```
-u, --url: Required. Target URL (e.g., http://example.com).
-t, --type: Required. Specifies the test type to perform:
cl.te: Test for Content-Length vs. Transfer-Encoding vulnerability.
te.cl: Test for Transfer-Encoding vs. Content-Length vulnerability.
all: Run both cl.te and te.cl tests sequentially.
```
Examples
1. Run a CL.TE test:
```bash
python spydirbyte.py -u http://example.com -t cl.te
```
2. Run a TE.CL test:
```bash
python spydirbyte.py -u http://example.com -t te.cl
```
3. Run all tests:
```bash
python spydirbyte.py -u http://example.com -t all
```

