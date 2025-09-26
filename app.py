from flask import Flask, request
import requests
import os

TOKEN = os.environ.get('BOT_TOKEN')
RELAY_URL = os.environ.get('RELAY_URL')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def relay():
    update = request.json
    if update:
        requests.post(f"{RELAY_URL}", json=update)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
