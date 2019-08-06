import os
from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)