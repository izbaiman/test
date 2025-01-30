from flask import Flask
import logging

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.debug('Home route was accessed')
    return 'Hello, World'

if __name__ == '__main__':
    app.run(debug=True)
