from flask import Flask, jsonify, render_template
from flask_cors import CORS
import detection

app = Flask(__name__)
CORS(app)



@app.route('/api/endpoint')
def index():
    result = detection.essen()
    message = f"User is {result}"
    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(debug=True)