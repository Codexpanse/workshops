import http.server
import socketserver

with socketserver.TCPServer(("", 8080), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Server started...")
    httpd.serve_forever()
