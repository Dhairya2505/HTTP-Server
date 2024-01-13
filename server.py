from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._headers_buffer=[]
        file_content = ''
        if (self.path == '/' or self.path == '/index'):
            self.path = '/index.html'
            try:
                with open(self.path[1:], 'r') as file:
                    file_content = file.read()
                    self.send_response(200)
            except FileNotFoundError:
                file_content = 'File not found'
                self.send_response(404)
            


        elif(self.path=='/index/login' or self.path == '/login'):
            self.path = '/login.html'
            try:
                with open(self.path[1:], 'r') as file:
                    file_content = file.read()
                    self.send_response(200)
            except FileNotFoundError:
                file_content = 'Login page not found'
                self.send_response(404)


        self.end_headers()
        self.wfile.write(bytes(file_content,'utf-8'))



    def do_POST(self):
        self._headers_buffer=[]
        if(self.path == '/afterlogin'):
            self.path = '/afterlogin.html'
            file_content = open(self.path[1:]).read()
            content_length = int(self.headers['Content-Length'])
            post_data = parse_qs(self.rfile.read(content_length).decode('utf-8'))
            

            user = post_data.get('username')[0]
            pword = post_data.get('password')[0]

            print(user)
            print(pword)

            self.send_response(200)
            self.send_header('Content-type','text/html')

            self.end_headers()
            self.wfile.write(bytes(file_content,'utf-8'))

            


def main():
    PORT = 9000
    server = HTTPServer(('',PORT),echoHandler)
    print('Server Running on "localhost:9000"')
    server.serve_forever()


if __name__ == "__main__":        
    main()
