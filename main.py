from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'goatbypassersontop'
BASE_URL = 'http://45.90.13.151:6132/api/bypass'

@app.route('/bypass', methods=['GET'])
def bypass():
    link = request.args.get('link')

    if not link:
        return jsonify({'error': 'Link parameter is required'}), 400

    response = requests.get(BASE_URL, params={'link': link, 'api_key': API_KEY})

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to bypass the link'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
