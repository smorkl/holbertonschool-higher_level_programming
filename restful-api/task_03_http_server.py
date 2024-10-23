from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Simpleseerver(BaseHTTPRequestHandler):
    def do_GET(self):
    
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return
        
        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
            return
        
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            return
            
        elif self.path == "/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(data).encode())
            return
        
        else :
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")
            return
            
def run(server_class=HTTPServer, handler_class=Simpleseerver, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()