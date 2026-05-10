from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Basic Monitoring App</title>
    <style>
        body {
            background-color: #0f172a;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .card {
            background: #1e293b;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
        }

        h1 {
            color: #38bdf8;
            margin-bottom: 10px;
        }

        p {
            font-size: 18px;
            color: #cbd5e1;
        }

        .status {
            margin-top: 20px;
            padding: 10px;
            background: #16a34a;
            border-radius: 10px;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>🚀 Kubernetes Monitoring App</h1>
        <p>Version 5 Successfully Deployed</p>

        <div class="status">
            ✅ Application Running Healthy
        </div>
    </div>

</body>
</html>
"""

class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # Simulate slight processing delay (helps HPA testing)
        time.sleep(0.2)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(HTML_PAGE.encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)

    print("Server running on port 8000...")

    server.serve_forever()