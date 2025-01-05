from flask import Flask
import socket

app = Flask(__name__)

@app.route('/data')
def data():
    hostname = socket.gethostname()
    return f"Hello from backend service running on {hostname}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)