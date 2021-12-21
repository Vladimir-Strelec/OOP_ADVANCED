class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) < 15:
            self.__username = value
            return
        raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_lenght(value) and self.contains_uppercase(value) and self.contains_number(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def is_lenght(self, password):
        return len(password) >= 8

    def contains_uppercase(self, password):
        return any([i for i in password if i.isupper()])

    def contains_number(self, password):
        return any([i for i in password if i.isdigit()])

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.__password)}'


# profile_with_invalid_username = Profile("Too_long_username", "Any")
# profile_with_invalid_password = Profile("My_username", "My-password")
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
