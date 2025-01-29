from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/greet', methods=['GET'])
def greet():
    return {'message': 'Hello from Flask API!'}

if __name__ == '__main__':
    app.run(debug=True)
