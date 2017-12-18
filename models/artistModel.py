class ArtistModel():
    def __init__(self, bornDate, desc, imageURL, topSongs):
        self.bornDate = bornDate
        self.desc = desc
        self.imageURL = imageURL
        self.topSongs = topSongs

    def json(self):
        return {"bornDate": self.bornDate, "description": self.desc, "imageURL": self.imageURL, "Top Songs": self.topSongs}
