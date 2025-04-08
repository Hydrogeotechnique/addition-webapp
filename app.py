from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # Rendre le fichier index.html depuis le dossier templates
    return render_template('index.html')

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

