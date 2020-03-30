import platform

# conditionally import based on py2 vs py3
if platform.python_version_tuple()[0] == "2":
    import SimpleHTTPServer
    import SocketServer
    from urlparse import parse_qs, urlparse
else:
    import http.server as SimpleHTTPServer
    import socketserver as SocketServer
    from urllib.parse import parse_qs, urlparse

import sh
import click

@click.command()
@click.argument("host", default="0.0.0.0")
@click.argument("port", type=int, default=8000)
def main(host, port):
    httpd = SocketServer.TCPServer((host, port), H)
    print("Serving:", host + ":" + str(port))
    httpd.allow_reuse_address = True
    httpd.serve_forever()

class H(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self, *args, **kwargs):
        url = urlparse(self.path)
        qs = parse_qs(url.query)
        host = qs.get("ping")
        if host:
            try:
                res = str(sh.ping("-c", "1", host))
            except Exception:
                res = "Couldn't ping " + host
        else:
            res = "Hello world!\nUse ?ping=HOST to ping a host."
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-length", len(res))
        self.end_headers()
        self.wfile.write(bytearray(res, "utf8"))

if __name__ == "__main__":
    main()
