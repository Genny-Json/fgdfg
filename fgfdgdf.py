import ssl
import socketserver
from pathlib import Path

import http.server

# Configuration
PORT = 8443
CERTFILE = "server.crt"
KEYFILE = "server.key"
### gg

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTFILE, KEYFILE)

# Create HTTPS server
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"HTTPS server running on https://localhost:{PORT}")
    httpd.serve_forever()