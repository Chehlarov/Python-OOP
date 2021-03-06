from typing import List
from project_albums.song import Song


class Album:
    name: str
    songs: List[Song]
    published: bool

    def __init__(self, name, *args, published=False):
        self.name = name
        self.published = published
        self.songs = []
        for el in args:
            self.add_song(el)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        for el in self.songs.copy():
            if el.name == song_name:
                self.songs.remove(el)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        song_info_list = [el.get_info() for el in self.songs]
        return f"Album {self.name}\n" + "\n".join(song_info_list)