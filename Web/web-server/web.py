from http.server import BaseHTTPRequestHandler, HTTPServer
Host = "127.0.0.1"
port = 7777
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write("""
                            <!DOCTYPE html>
                            <html>
                            <head>
                                <title>Python Web Server</title>
                            </head>
                         <body>
                        <h1>Hello, Iam Your Server </h1>
                </body>
                         </html>""".encode("UTF-8"))

class HTTPserver(HTTPServer):
    def __init__(self, host, port):
        server_addrs = (host, port)
        HTTPServer.__init__(self, server_addrs, RequestHandler)

def run_server(host, port):
    server = HTTPserver(host, port)
    print(f"listen at {port}")
    server.serve_forever()
    server.socket.close()


run_server(Host, port)

