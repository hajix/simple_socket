import BaseHTTPServer

def keep_running():
	return True

def run_while_true(server_class = BaseHTTPServer.HTTPServer,handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    while keep_running():
        httpd.handle_request()

run_while_true()
