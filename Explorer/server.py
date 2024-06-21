from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import requests

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        file_path = self.path[1:]  # Remove the leading '/'
        if os.path.exists(file_path):
            return SimpleHTTPRequestHandler.do_GET(self)
        else:
            url = f"https://vision.cs.stonybrook.edu/ryan_adobe/all/{file_path}"
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                self.send_response(200)
                self.send_header("Content-type", response.headers["Content-Type"])
                self.end_headers()
                self.wfile.write(response.content)
            else:
                self.send_response(301)
                self.send_header("Location", url)
                self.end_headers()

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all available interfaces, port 8000
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"Serving on http://{server_address[0]}:{server_address[1]}")
    httpd.serve_forever()