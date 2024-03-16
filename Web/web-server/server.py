import http.server
import socketserver
port = 8888
ip = "localhost"
Handler = http.server.SimpleHTTPRequestHandler
server = socketserver.TCPServer((ip, port), Handler)
def run():
    print("Serving at port", port)
    server.serve_forever()
run()
