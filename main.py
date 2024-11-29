from http.server import BaseHTTPRequestHandler, HTTPServer
import os

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        routes = {
            '/': 'html/main.html',
            '/main.html': 'html/main.html',
            '/catalog.html': 'html/catalog.html',
            '/category.html': 'html/category.html',
            '/contact.html': 'html/contact.html',
        }

        file_path = routes.get(self.path)

        if file_path and os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write(bytes(html_content, "utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><body><h1>404 Not Found</h1></body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
