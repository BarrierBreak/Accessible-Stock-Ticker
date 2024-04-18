from flask import Flask, render_template
import json
import time

app = Flask(__name__)

# Dummy stock data
dummy_data = [
    {"nifty_bank": 35000, "sensex": 50000, "nifty_50": 15000},
    {"nifty_bank": 35200, "sensex": 48000, "nifty_50": 15100},
    {"nifty_bank": 34800, "sensex": 49800, "nifty_50": 10000}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return json.dumps(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)
