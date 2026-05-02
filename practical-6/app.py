from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Optimized Docker Image Demo", "hostname": socket.gethostname(), "practical": "DevOps No. 6"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
