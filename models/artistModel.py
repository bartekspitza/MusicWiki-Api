class ArtistModel():
    def __init__(self, bornDate, desc):
        self.bornDate = bornDate
        self.desc = desc

    def json(self):
        return {"bornDate": self.bornDate, "description": self.desc}
