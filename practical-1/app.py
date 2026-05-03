from flask import Flask, jsonify
import os, socket, datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Jenkins CI/CD Pipeline Demo",
        "practical": "DevOps Practical No. 1",
        "author": "Nilesh Malekar",
        "pipeline": "GitHub -> Jenkins -> Docker -> Kubernetes",
        "container": socket.gethostname(),
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "flask-p1"}), 200

@app.route('/info')
def info():
    return jsonify({
        "python": os.sys.version.split()[0],
        "hostname": socket.gethostname(),
        "platform": "Kubernetes via Jenkins Pipeline"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
