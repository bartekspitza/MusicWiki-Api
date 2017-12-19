class ArtistModel():
    def __init__(self, imageURL, desc, topSongs):
        self.imageURL = imageURL
        self.desc = desc
        self.topSongs = topSongs

    def json(self):
        return {"description": self.desc, "imageURL": self.imageURL, "Top Songs": self.topSongs}
