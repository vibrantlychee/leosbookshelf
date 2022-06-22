class TextBlock:
    def __init__(self, content: str, bold: bool, italics: bool, underline: bool, link: str):
        self.content = content
        self.bold = bold
        self.italics = italics
        self.underline = underline
        self.link = link

    def __str__(self):
        return self.content        

class ImageBlock:
    def __init__(self, url: str, captions: list):
        self.url = url
        self.captions = captions

    def __str__(self):
        out = self.url + "\n"
        for caption in self.captions:
            out += str(caption)
        
        return out

class ParagraphBlock:
    def __init__(self, children: list):
        self.children = children

    def __str__(self):
        out = ""
        for child in self.children:
            out += str(child)

        return out

class TableBlock:
    def __init__(self, name: str, year: str, artist: str, quote: str):
        self.name = name
        self.year = year
        self.artist = artist
        self.quote = quote

    def __str__(self):
        return self.name + "/" + self.year+ "/" + self.artist + "/" + self.quote

class TitleBlock:
    def __init__(self, title: str, favicon_url: str, poster_url: str):
        self.title = title
        self.favicon_url = favicon_url
        self.poster_url = poster_url

    def __str__(self):
        return self.title + self.favicon_url + self.poster_url