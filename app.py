from http.server import BaseHTTPRequestHandler, HTTPServer

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"App Version 3")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    server.serve_forever()

