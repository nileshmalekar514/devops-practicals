from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "GitHub Actions CI/CD Demo",
        "practical": "DevOps Practical No. 3",
        "author": "Nilesh Malekar",
        "ci": "GitHub Actions - PR trigger + unit tests + Slack notify",
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
        "ci_tool": "GitHub Actions"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
