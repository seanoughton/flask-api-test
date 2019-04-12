from flask import Flask,render_template, request
from flask-restful import Api, Resource

app = Flask(__name__)


@app.route('/', methods=['GET','POST']):
    def index():
        return "something"


if __name__ == '__main__':
    app.run(debug=True)
