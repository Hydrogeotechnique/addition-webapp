from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS

app = Flask(__name__)
CORS(app)  # Appliquer CORS à toutes les routes

@app.route('/')
def home():
    return 'Hello, Flask fonctionne !'

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    try:
        result = float(a) + float(b)
    except (TypeError, ValueError):
        return jsonify({'error': 'Entrées invalides'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
