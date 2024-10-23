from flask import Flask, jsonify

app = Flask(__name__)

# Sample route for API
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


