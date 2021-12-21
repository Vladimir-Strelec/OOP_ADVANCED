from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for r in range(len(self.photos)):
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)
                return f"{label} photo added successfully on page {r+1} slot {len(self.photos[r])}"
        return f"No more free slots"

    def display(self):
        result = ''
        for r in self.photos:
            result += "-----------\n"
            result += ' '.join([str([]) for _ in r])
            result += '\n'
        result += "-----------\n"
        return result


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())