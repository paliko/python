import datetime,http.server #v dvojkovym pythonu BaseHTTPServer
class odpoved(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        html = """<html><body>
        <h1>Vita Vas Honzuv server !!!!</h1>
        <h3>Je prave : %s</h3>
        </body></html>""" % datetime.datetime.now()
        self.wfile.write(bytes(html,encoding="ascii"))
server = http.server.HTTPServer(('',80),odpoved) #tohle vytvori instanci serveru
server.serve_forever() # tohle spusti smycku toho serveru
