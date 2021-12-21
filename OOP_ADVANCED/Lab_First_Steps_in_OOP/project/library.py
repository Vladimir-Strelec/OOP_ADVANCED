from Person_1.project import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):

        for obj in self.user_records:
            if user.username == obj.username:
                return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user: User):
        for obj in self.user_records:
            if user.username == obj.username:
                self.user_records.remove(user)
                return
        return f"We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str):
        for obj in self.user_records:
            if obj.user_id == user_id and obj.username != new_username:
                obj.username = new_username
                if obj.username in self.rented_books:
                    self.rented_books[new_username] = {}
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
            if obj.user_id == user_id and obj.username == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"