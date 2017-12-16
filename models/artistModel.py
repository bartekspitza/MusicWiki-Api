class ArtistModel():
    def __init__(self, bornDate, desc, imageURL):
        self.bornDate = bornDate
        self.desc = desc
        self.imageURL = imageURL

    def json(self):
        return {"bornDate": self.bornDate, "description": self.desc, "imageURL": self.imageURL}
