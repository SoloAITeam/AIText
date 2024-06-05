from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AIRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow requests from any origin
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')  # Allow POST and OPTIONS methods
        self.send_header('Access-Control-Allow-Headers', 'Content-type')  # Allow Content-type header
        self.end_headers()

    def do_POST(self):
        self._set_response()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # Here you can process the POST data as needed
        # For example, you can pass it to your AI model and generate a response
        response_data = {"response": "This is the AI response"}
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def do_OPTIONS(self):
        self._set_response()

def run_server(server_class=HTTPServer, handler_class=AIRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    
