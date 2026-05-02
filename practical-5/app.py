from flask import Flask, jsonify
import redis, os, socket

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    try:
        count = cache.incr('hits')
        redis_status = "connected"
    except Exception as e:
        count = -1; redis_status = str(e)
    return jsonify({"message": "Multi-container Flask + Redis App", "hits": count, "redis": redis_status, "container": socket.gethostname(), "practical": "DevOps No. 5", "author": "Nilesh Malekar"})

@app.route('/health')
def health():
    try:
        cache.ping()
        return jsonify({"status": "healthy", "redis": "up"}), 200
    except:
        return jsonify({"status": "degraded", "redis": "down"}), 200

@app.route('/info')
def info():
    return jsonify({"service": "flask-web", "redis_host": "redis:6379", "hostname": socket.gethostname()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
