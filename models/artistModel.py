class ArtistModel():
    def __init__(self, desc, imageURL, topSongs):
        self.desc = desc
        self.imageURL = imageURL
        self.topSongs = topSongs

    def json(self):
        return {"description": self.desc, "imageURL": self.imageURL, "Top Songs": self.topSongs}
