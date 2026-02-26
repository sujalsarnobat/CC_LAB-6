import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = socket.gethostname()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f"<h1>Served by backend: {hostname}</h1>".encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()
