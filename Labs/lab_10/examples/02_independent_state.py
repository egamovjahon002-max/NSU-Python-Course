class Playlist:
    def __init__(self):
        self.songs = []
    def add(self, song):
        self.songs.append(song)

first = Playlist()
second = Playlist()
first.add("Song A")
print(first.songs)
print(second.songs)
