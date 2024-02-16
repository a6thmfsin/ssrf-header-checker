#!/usr/bin/python3

import requests

def read_urls_from_file(file_path):
    with open(file_path, "r") as file:
        urls = file.readlines()
    urls = [url.strip() for url in urls]
    return urls

headers = {
    "X-Originating-IP": "collab",
    "X-Forwarded-For": "collab",
    "X-Forwarded": "collab",
    "Forwarded-For": "collab",
    "X-Remote-IP": "collab",
    "X-Remote-Addr": "collab",
    "X-ProxyUser-Ip": "collab",
    "Client-IP": "collab",
    "True-Client-IP": "collab",
    "Cluster-Client-IP": "collab",
    "Host": "collab",
    "X-Forwarded-Host": "collab",
    "X-Host": "collab",
    "X-Forwarded-Server": "collab",
    "X-HTTP-Host-Override": "collab",
    "Forwarded": "collab",
    "Via": "collab",
    "Origin": "collab"
}

def send_requests(urls):
    with open("sent-requests-verbose.txt", "w") as f:
        for url in urls:
            try:
                response = requests.get(url, headers=headers)
                f.write(f"URL: {url}\nHeaders: {response.request.headers}\n\n")
            except requests.exceptions.RequestException as e:
                print(f"error {url}: {e}")

if __name__ == "__main__":
    input_file_path = input("input endpoints (path): ")
    urls = read_urls_from_file(input_file_path)
    send_requests(urls)
