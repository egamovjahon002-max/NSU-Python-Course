class Playlist:
    def __init__(self):
        self._songs = ["Song A"]
    def get_songs(self):
        return self._songs.copy()

playlist = Playlist()
copy = playlist.get_songs()
copy.append("Song B")
print(copy)
print(playlist.get_songs())
