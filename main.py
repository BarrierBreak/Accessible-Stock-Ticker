import random
import threading
import time
from flask import Flask, render_template

app = Flask(__name__)

class StockTicker:
    def __init__(self, symbols):
        self.symbols = symbols
        self.prices = {symbol: 100.0 for symbol in symbols}  # Initial price is set to 100 for all symbols
        self.lock = threading.Lock()

    def update_prices(self):
        while True:
            with self.lock:
                for symbol in self.symbols:
                    # Simulating price changes with random fluctuations
                    change = random.uniform(-1, 1) * 5  # Maximum price change of $5
                    self.prices[symbol] += change
            time.sleep(2)  # Update prices every 2 seconds

    def get_prices(self):
        with self.lock:
            return self.prices

ticker = StockTicker(["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"])

@app.route('/')
def index():
    return render_template('index.html', symbols=ticker.symbols)

@app.route('/prices')
def prices():
    return ticker.get_prices()

if __name__ == "__main__":
    threading.Thread(target=ticker.update_prices, daemon=True).start()
    app.run(debug=True)


