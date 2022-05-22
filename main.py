import os

from http.server import (BaseHTTPRequestHandler, 
                         HTTPServer)


class handler_get(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = os.environ.get('CONTENT')
        self.wfile.write(bytes(message, 'utf8'))

with HTTPServer(
    ('0.0.0.0', int(os.environ.get('PORT'))), handler_get) as server:
    server.serve_forever()