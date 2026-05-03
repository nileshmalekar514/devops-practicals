from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "GitLab CI/CD Pipeline Demo",
        "practical": "DevOps Practical No. 2",
        "author": "Nilesh Malekar",
        "pipeline": "GitLab CI -> Test -> Build -> Deploy to EC2",
        "container": socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "python": os.sys.version.split()[0],
        "hostname": socket.gethostname(),
        "deployed_via": "GitLab CI Pipeline"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
