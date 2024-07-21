"""
MIT License

Copyright (c) 2024 Julian Stiebler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Created: 15.07.2024
# Last edited: 17.07.2024
"""

import argparse
import os
from secureRequests.secureRequests import SecureRequests

def main():
    parser = argparse.ArgumentParser(description="Fetch data securely or unsafely from a URL")
    parser.add_argument('--fetch', metavar='URL', type=str, help="Fetch data from the specified URL")
    parser.add_argument('--unsafe', action='store_true', help="Set unsafe request")
    parser.add_argument('--write', metavar='FILE_PATH', type=str, help="Write response content to a file")
    parser.add_argument('--method', metavar='METHOD', type=str, default='GET', choices=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
                        help="HTTP method for the request (default: GET)")
    args = parser.parse_args()

    secure_request = SecureRequests(unsafe=args.unsafe, fetchCertificate=True, useTLS=True)

    if args.fetch:
        response = secure_request.makeRequest(args.fetch, method=args.method)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")

        if args.write:
            writeFilePath = os.path.abspath(args.write)
            with open(writeFilePath, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Response content written to: {writeFilePath}")

if __name__ == "__main__":
    main()
