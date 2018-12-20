import http.server
import socketserver

host = "localhost"
port = 8080

server = socketserver.TCPServer((host, port), http.server.SimpleHTTPRequestHandler)

print("Server started...")
server.serve_forever()
