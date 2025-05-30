import re
from domain.user import User
from storage.user_repository import UserRepository

class UserFieldValidationException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class FatalUserCreationException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

class UserBuilder:
    """
    Builder pattern for User model, contains fields validation.
    Throws `UserFieldValidationException`, u should try-catch it when building.
    Throws `FatalUserCreationException` when the creation operation cannot be performed for the provided data.
    """

    def __init__(self) -> None:
        self._username = None
        self._name = None
        self._email = None
        self._phone = None
        self._age = None

    def username(self, username: str) -> "UserBuilder":
        if not username:
            raise UserFieldValidationException("Username cannot be empty")
        user = UserRepository().find_user_by_username(username)
        if user is not None:
            raise FatalUserCreationException("User with this username is already in db, can not create")

        self._username = username
        return self

    def name(self, name: str) -> "UserBuilder":
        if not name:
            raise UserFieldValidationException("Username cannot be empty")

        self._name = name
        return self

    def email(self, email: str) -> "UserBuilder":
        regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        if not re.match(regex, email):
            raise UserFieldValidationException("User's email must be in a valid format -> example@domain.com")

        self._email = email
        return self

    def phone(self, phone: str) -> "UserBuilder":
        regex = r'^\+[0-9]{7,15}$'
        if not re.match(regex, phone):
            raise UserFieldValidationException("User's phone number must be in a valid, international format -> plus followed by from 7 to 15 digits")

        self._phone = phone
        return self

    def age(self, age: str) -> "UserBuilder":
        if not age.isdigit():
            raise UserFieldValidationException("User's age must be a digit")
        elif int(age) <= 0:
            raise UserFieldValidationException("User's age must be a positive integer")

        self._age = int(age)
        return self

    def build(self) -> User | None:
        if not self._username or not self._name or not self._email or not self._phone or not self._age:
            return None

        return User(self._username, self._name, self._email, self._phone, self._age)
