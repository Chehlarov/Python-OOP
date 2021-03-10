import math
class PhotoAlbum:
    photos: [[str]]

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return "No more free spots"

    def display(self):
        out = ("-" * 11 + "\n")
        for page in self.photos:
            out += (str("[] " * len(page)).strip() + "\n")
            out += ("-" * 11 + "\n")
        return out

# album = PhotoAlbum(2)
#
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
#
# # print(album.display())
# album = PhotoAlbum(1)
# album.add_photo("baby")
# album.add_photo("first grade")
# album.add_photo("eight grade")
# album.add_photo("party with friends")
# print(album.display())
# # print("should be")
# # print("-----------\n[] [] [] []\n-----------\n")