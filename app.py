from flask import Flask, request, jsonify
from yahooquery import Ticker
from datetime import datetime
import pytz
import random
import json
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "API to generate values for B3 shares."


@app.route('/stocks/<stock_code>', methods=['GET'])
def generate_value_share(stock_code):
    ticker_stock = Ticker(stock_code)
    result = ticker_stock.history(period="7d",  interval="5m")
    result.reset_index(inplace=True)

    index = random.randrange(0, result.shape[0], 1)
    result = result.iloc[[index]]

    retorn = {'code': stock_code,
               'dateTime': datetime.now(pytz.timezone('AMERICA/Sao_Paulo')).isoformat(),
               'value': result['close'].values[0]}

    return json.dumps(retorn), 200


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
