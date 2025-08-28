from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

# 模拟数据接口
@app.route('/data')
def get_data():
    return jsonify({
        "time": int(time.time()),
        "temperature": round(random.uniform(20, 30), 2),
        "humidity": round(random.uniform(40, 60), 2),
        "heart_rate": random.randint(60, 100)
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
