from flask import Flask, render_template
import redis

app = Flask(__name__)

# Connect to Redis (IMPORTANT: host is service name)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    count = redis_client.incr('page_views')
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
