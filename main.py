from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API endpoint and key
API_URL = 'https://madkung.vercel.app/fluxus-api'
API_KEY = 'XqzyaenZishd33axPYPz'

@app.route('/fluxus', methods=['GET'])
def fluxus():
    # Ambil parameter URL dari permintaan
    target_url = request.args.get('url')

    # Pastikan parameter URL ada
    if not target_url:
        return jsonify({'error': 'URL parameter is required'}), 400

    # Buat permintaan ke API eksternal
    try:
        response = requests.get(API_URL, params={'url': target_url, 'api_key': API_KEY})
    except Exception as e:
        return jsonify({'error': f'Failed to fetch data from external API: {str(e)}'}), 500

    # Periksa apakah permintaan berhasil
    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from external API'}), response.status_code

    # Ambil data JSON dari respons
    data = response.json()

    # Ganti teks 'ethos' dengan 'api' dalam data respons
    modified_data = str(data).replace('mad6453', 'famzz')

    # Kembalikan data yang dimodifikasi sebagai JSON
    return jsonify(eval(modified_data))

if __name__ == '__main__':
    app.run(debug=True)
