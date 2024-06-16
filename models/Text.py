

class Text:

    def __init__(self, text: str, encoding: str = "utf-8"):
        self.text = text
        self.encoding = encoding

    def __str__(self):
        return self.text
    
    def to_bytes(self):
        return self.text.encode(self.encoding)