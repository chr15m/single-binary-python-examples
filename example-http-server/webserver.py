from __future__ import print_function

from os.path import join, dirname
from os import getcwd
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
            ct = "text/plain"
            try:
                res = str(sh.ping("-c", "1", host))
            except Exception:
                res = "Couldn't ping " + host
        else:
            ct = "text/html"
            with open(join(dirname(__file__), "pages", "index.html")) as f:
                res = f.read()
        self.send_response(200)
        self.send_header("Content-type", ct)
        self.send_header("Content-length", len(res))
        self.end_headers()
        self.wfile.write(bytearray(res, "utf8"))

if __name__ == "__main__":
    main()
