import os

class Config:
    STORAGE_FILE_PATH = os.getenv("STORAGE_FILE_PATH", "data/users.json")
