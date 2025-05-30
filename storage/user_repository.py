import os
from configuration.app_config import Config
from domain.user import User
import json

class UserRepository:
    """
    Singleton class that executes all data access layer operations on json stored users
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.storage_path = Config.STORAGE_FILE_PATH
        if not os.path.exists(self.storage_path):
           with open(self.storage_path, 'w') as users_file:
               json.dump({"users": {}}, users_file)

    def find_user_by_username(self, username: str) -> User | None:
        with open(self.storage_path, 'r') as users_file:
            users_data = json.load(users_file)
            user = users_data["users"].get(username)
            if user:
                return User(
                    username,
                    **user
                )

            return None

    def save_user(self, user: User) -> None:
        with open(self.storage_path, 'r') as users_file:
            users_data = json.load(users_file)

        users_data["users"][user.username] = {
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "age": user.age
        }

        with open(self.storage_path, 'w') as users_file:
            json.dump(users_data, users_file)
