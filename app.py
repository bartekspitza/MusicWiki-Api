from flask import Flask
from flask_restful import Api
from resources.artist import Artist
from resources.lyrics import Lyrics
totalRequestCount = 0
app = Flask(__name__)
api = Api(app)


api.add_resource(Artist, "/artist/<string:artist>")
api.add_resource(Lyrics, "/lyrics")

@app.route("/stats")
def page():
    return "Total request to this API so far: " + str(totalRequestCount)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
