from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":  # Respond to requests for the root path "/"
            self.send_response(200)  # Send a successful response (code 200)
            self.send_header('Content-type', 'text/plain')  # Set the content type as plain text
            self.end_headers()  # Send the headers to the client
            self.wfile.write(b"Hello, this is a simple API!")  # Send the response content (replace with your desired content)
            return
        
        if self.path == "/data":  # Respond to requests for the "/data" path
            # Prepare the JSON data
            data = {"name": "John", "age": 30, "city": "New York"}

            # Set the content type header
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            # Convert data to JSON string
            json_data = json.dumps(data)
            # Encode data as bytes
            encoded_data = json_data.encode()
            # Send the JSON data
            self.wfile.write(encoded_data)
            return 
        
        if self.path == "/status":
            self.send_response(200)  # Send a successful response (code 200)
            self.send_header('Content-type', 'text/plain')  # Set the content type as plain text
            self.end_headers()  # Send the headers to the client
            self.wfile.write(b"ok")  # Send the response content (replace with your desired content)
            return
        
        if self.path == "/info":
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            info_string = json.dumps(info_data)  # Convert dictionary to JSON string
            encoded_data = info_string.encode()  # Encode the string as bytes

            # Send the response headers
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')  # Set content type to JSON
            self.end_headers()

            # Write the response content
            self.wfile.write(encoded_data)  

        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"404 Not Found")

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
