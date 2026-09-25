#!/usr/bin/env python3
import http.server
import socketserver
import subprocess
import sys

PORT = 8045

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Silent logging or brief log
        pass

    def do_GET(self):
        self._proxy_request("GET")

    def do_POST(self):
        self._proxy_request("POST")

    def _proxy_request(self, method):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""

        # Build curl.exe command
        cmd = [
            "curl.exe",
            "-s",
            "-X", method,
            f"http://127.0.0.1:8045{self.path}",
        ]
        
        # Forward auth and content-type headers
        auth = self.headers.get("Authorization")
        if auth:
            cmd.extend(["-H", f"Authorization: {auth}"])
        c_type = self.headers.get("Content-Type")
        if c_type:
            cmd.extend(["-H", f"Content-Type: {c_type}"])

        if method == "POST":
            cmd.extend(["-d", "@-"])

        try:
            proc = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE if method == "POST" else None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = proc.communicate(input=body if method == "POST" else None)
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(stdout)))
            self.end_headers()
            self.wfile.write(stdout)
        except Exception as e:
            err_msg = str(e).encode("utf-8")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(err_msg)))
            self.end_headers()
            self.wfile.write(err_msg)

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run():
    with ReusableTCPServer(("127.0.0.1", PORT), ProxyHandler) as httpd:
        print(f"[WSL Antigravity Bridge] Listening on 127.0.0.1:{PORT} -> forwarding to Windows...")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == "__main__":
    run()
