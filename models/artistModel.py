class ArtistModel():
    def __init__(self, name, desc, imageURL, topSongs):
        self.name = name
        self.desc = desc
        self.imageURL = imageURL
        self.topSongs = topSongs

    def json(self):
        return {"name": self.name, "description": self.desc, "imageURL": self.imageURL, "Top Songs": self.topSongs}
