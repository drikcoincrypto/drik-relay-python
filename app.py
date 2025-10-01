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
        try:
            r = requests.post(RELAY_URL, json=update, verify=False, timeout=5)
            print("Test relay status code:", r.status_code)
            print("Test relay response body:", r.text)
        except Exception as e:
            print("Error sending request:", e)
    return {'status': 'ok'}

if __name__ == '__main__':
    # تست اتصال مستقیم به مقصد در زمان بوت
    try:
        print("Testing direct connection to relay target:", RELAY_URL)
        r = requests.get(RELAY_URL, verify=False, timeout=5)
        print("Initial test status code:", r.status_code)
        print("Initial test body:", r.text[:200])
    except Exception as e:
        print("Initial connection test failed:", e)

    app.run(host='0.0.0.0', port=10000)
