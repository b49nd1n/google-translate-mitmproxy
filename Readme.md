## Mitmproxy over google translate

Small addon for mitmproxy to proxy traffic throw google translate

How to use:

1. install mitmproxy (e.g apt install mitmproxy)
2. pip -r requirements.txt
3. mitmproxy -s proxy.py --no-http2
4. (opt) u also can import ca-cert from .mitmproxy to your browser
