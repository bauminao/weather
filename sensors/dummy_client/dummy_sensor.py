#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
    # Send response status code
    self.send_response(200)
 
    # Send headers
    self.send_header('Content-type','text/html')
    self.end_headers()
 
    # Send message back to client

    with open("./data_fresh.json",'r', encoding='utf-8-sig') as json_file:
      json_data = json.load(json_file)
    json_html   = json.dumps(json_data, indent=4, sort_keys="True").replace('\n','<br>\n').replace(' ','&nbsp')

    # Write content as utf-8 data
    self.wfile.write(bytes(json_html, "utf8"))
    return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 2905)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()
