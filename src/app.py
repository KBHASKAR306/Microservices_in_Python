from flask import Flask, jsonify, render_template
import socket

def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )
    
@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, Ip=ip)
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)