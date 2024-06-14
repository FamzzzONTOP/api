from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/bypass', methods=['GET'])
def bypass():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    api_url = "https://2c8f98d8-9741-4ae2-b2c4-3e9d12cc68e1-00-1huumoqlhh1yg.sisko.replit.dev/bypass"
    params = {'url': target_url}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)