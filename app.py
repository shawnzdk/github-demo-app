from http.server import BaseHTTPRequestHandler, HTTPServer
import os

PORT = int(os.environ.get("PORT", "8085"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = b"""
        <html>
        <head><title>GitHub Deployment Demo</title></head>
        <body style="font-family:Arial;background:#111827;color:white;padding:50px;">
            <h1>GitHub Deployment Successful</h1>
            <p>This application was deployed automatically from GitHub.</p>
            <p>Platform: Proxmox IaC Portal</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
