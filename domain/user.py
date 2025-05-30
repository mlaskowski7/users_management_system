class User:
    def __init__(self, username: str, name: str, email: str, phone: str, age: int) -> None:
        self.username = username
        self.name = name
        self.email = email
        self.phone = phone
        self.age = age

    def __str__(self) -> str:
        return f'{self.username.upper()} ->\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nAge: {self.age}'
