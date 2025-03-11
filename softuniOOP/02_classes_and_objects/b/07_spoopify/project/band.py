
from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for x in self.albums:
            if album_name == x.name and x.published:
                return "Album has been published. It cannot be removed."
            elif album_name == x.name:
                self.albums.remove(x)
                return f"Album {x.name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        to_return = f"Band {self.name}"
        for y in self.albums:
            to_return += f"\n{y.details()}"
        return to_return
