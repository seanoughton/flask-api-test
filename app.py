import Flask
from flask-restful import Api, Resource


@app.route('/'):
    def index():
        return "something"


if __name__ == '__main__':
    app.run(debug=True)
