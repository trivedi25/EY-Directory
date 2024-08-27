import pyodbc
import urllib
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
