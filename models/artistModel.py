class ArtistModel():
    def __init__(self, imageURL, desc, bornDate, topSongs):
        self.imageURL = imageURL
        self.desc = desc
        self.bornDate = bornDate
        self.topSongs = topSongs

    def json(self):
        return {"bornDate": self.bornDate, "description": self.desc, "imageURL": self.imageURL, "Top Songs": self.topSongs}
