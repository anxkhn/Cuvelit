from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data from the API
    url = "https://api.cuvette.tech/api/v1/externaljobs"
    response = requests.get(url)
    data = response.json()['data']
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)
