from http.server import BaseHTTPRequestHandler, HTTPServer

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == '/' or self.path == '/index'):
            self.path = '/index.html'
            try:
                file = open(self.path[1:]).read()
                self.send_response(200)
            except :
                file ='file not found'
                self.send_response(404)

        elif(self.path=='/index/login' or self.path == '/login'):
            self.path = '/login.html'
            try:
                file = open(self.path[1:]).read()
                self.send_response(200)
            except:
                file = 'login page not found'
                self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file,'utf-8'))
            

def main():
    PORT = 9000
    server = HTTPServer(('',PORT),echoHandler)
    print('Server Running on "localhost:9000"')
    server.serve_forever()


if __name__ == "__main__":        
    main()
