"""
http://stackoverflow.com/questions/2838244/get-open-tcp-port-in-python
Returns a socket to be used
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_open_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return str(port)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =54544)
