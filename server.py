"""
HTTP Basic Server
Contributors:
    :: H. Kamran [@hkamran80] (author)
License: MIT
"""

import http.server
import os
import socketserver


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Map .html, .css, .js, and image files automatically
        if (
            path.endswith(".html")
            or path.endswith(".css")
            or path.endswith(".js")
            or path.endswith(".jpg")
            or path.endswith(".jpeg")
            or path.endswith(".png")
            or path.endswith(".gif")
        ):
            return super().translate_path(path)

        if path == "/":
            return "index.html"

        # If the URL doesn't have an extension, try to serve .html first
        html_path = super().translate_path(path + ".html")
        if os.path.isfile(html_path):
            return html_path

        # If no .html file exists, serve the requested path with a .html extension
        return super().translate_path(path + ".html")


def serve(port: int) -> bool:
    # Create the server with the custom handler
    with socketserver.TCPServer(("", port), RequestHandler) as httpd:
        print(f"Serving at http://localhost:{port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            return False

    return False


if __name__ == "__main__":
    # Set the server port and directory
    port = os.getenv("PORT", 8080)
    directory = os.getcwd()
    os.chdir(directory)

    # Automatically generate URL mappings for HTML files in the current directory
    url_mappings = {}
    for filename in os.listdir(directory):
        if filename != "index.html" and filename.endswith(".html"):
            url_mappings["/" + os.path.splitext(filename)[0]] = filename

    serve_status = True
    while serve_status:
        try:
            serve_status = serve(port)
        except OSError as error:
            if error.errno == 98:  # Address already in use
                port += 1
