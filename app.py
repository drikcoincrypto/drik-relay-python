from flask import Flask, request
import requests
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# غیرفعال کردن هشدار SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

TOKEN = os.environ.get('BOT_TOKEN')
RELAY_URL = os.environ.get('RELAY_URL')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def relay():
    update = request.json
    if update:
        requests.post(RELAY_URL, json=update, verify=False)  # بی‌اعتبار کردن SSL
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
