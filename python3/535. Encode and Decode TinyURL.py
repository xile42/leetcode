class Codec:

    def __init__(self):

        self.id = 0
        self.db = dict()

    def encode(self, longUrl: str) -> str:

        self.db[self.id] = longUrl
        short_url = "http://tinyurl.com/{}".format(self.id)
        self.id += 1

        return short_url

    def decode(self, shortUrl: str) -> str:

        id = int(shortUrl.split("/")[-1])
        return self.db[id]
