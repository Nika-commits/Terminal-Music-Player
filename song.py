class Song:
    def __init__(self, title, artist, file_path):
        self.title = title
        self.artist = artist
        self.file_path = file_path

    def __str__(self):
        return f"{self.title} - {self.artist}"
