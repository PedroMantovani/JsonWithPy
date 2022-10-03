import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/upper', methods=['POST'])
def upper():
    json = request.get_json()
    first_name = json['first'].upper()
    last_name = json['last'].upper()
    valor = json['combo'].upper()
    return jsonify(first_name=first_name,last_name=last_name,valor=valor)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)