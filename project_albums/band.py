from typing import List
from project_albums.album import Album


class Band:
    name: str
    albums: List[Album]

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for el in self.albums.copy():
            if el.published:
                return "Album has been published. It cannot be removed."
            if el.name == album_name:
                self.albums.remove(el)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        album_info_list = [el.details() for el in self.albums]
        return f"Band {self.name}\n" + "\n".join(album_info_list)
