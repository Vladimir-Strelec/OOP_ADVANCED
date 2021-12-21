from setuptools.extension import Library


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library: Library):
        for k, v in library.rented_books.items():
            if book_name in v:
                return f"The book '{book_name}' is already rented and will be available in {v[book_name]} days!"

        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.rented_books[self.username] = {book_name: days_to_return}
            library.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name in self.books:
            self.books.remove(book_name)
            library.books_available[author].append(book_name)
            library.rented_books[self.username].pop(book_name)
            return
        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return ", ".join(sorted(self.books))

    def __repr__(self):
        return f"{self.user_id}, {self.username}, {self.books}"