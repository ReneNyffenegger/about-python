import SimpleHTTPServer
import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", 8888), Handler) # Listen at port 8888

httpd.serve_forever()
