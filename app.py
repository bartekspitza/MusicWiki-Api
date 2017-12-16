from flask import Flask
from flask_restful import Api
from resources.artist import Artist

app = Flask(__name__)
api = Api(app)


api.add_resource(Artist, "/artist/<string:artist>")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
