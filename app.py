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
        try:
            # ارسال با بی‌اعتبار کردن SSL و محدود کردن زمان انتظار
            requests.post(RELAY_URL, json=update, verify=False, timeout=10)
        except Exception as e:
            print("Error sending request:", e)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
