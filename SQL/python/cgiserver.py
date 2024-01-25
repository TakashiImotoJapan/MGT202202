import http.server
http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=8080, bind="0.0.0.0")
