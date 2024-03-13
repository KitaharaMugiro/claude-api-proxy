from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS  # CORSをインポート

# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
CORS(app)  # CORSをアプリケーションに適用

OPENAI_API_URL = 'https://anthropic.langcore.org/v1/messages'
# あなたのOpenAI APIキーをここに置いてください
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

@app.route('/openai-proxy', methods=['POST'])
def proxy_to_openai():
    # クライアントからのリクエストデータを取得
    client_data = request.json

    # OpenAI APIへのヘッダーを設定
    headers = {
        'Content-Type': 'application/json',
        "x-api-key": ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
    }
    print(headers)

    # OpenAI APIにリクエストを転送
    response = requests.post(OPENAI_API_URL, json=client_data, headers=headers)

    # OpenAIからのレスポンスをクライアントに返す
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=5000)