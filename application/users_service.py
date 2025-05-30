from application.user_builder import FatalUserCreationException, UserBuilder
from application.user_builder import UserFieldValidationException
from storage.user_repository import UserRepository

def create_user() -> None:
    print("You are creating a new user, please provide the following user details")
    builder = UserBuilder()

    create_steps = [
        ("username", builder.username),
        ("name", builder.name),
        ("email", builder.email),
        ("phone", builder.phone),
        ("age", builder.age)
    ]

    i = 0
    while i < len(create_steps):
        field, setter = create_steps[i]
        try:
            setter(input(f"{field.upper()}: "))
            i += 1
        except UserFieldValidationException as e:
            print(e)
        except FatalUserCreationException as e:
            print(e)
            return

    user = builder.build()
    if user:
        UserRepository().save_user(user)
        print("User was successfully saved!")

def read_user() -> None:
    username = input("Please provide username of the user that you are looking for: ")
    user = UserRepository().find_user_by_username(username)
    if user:
        print(f"Found the following user:\n{user}")
    else:
        print(f"User with username = {username} was not found!")

def update_user() -> None:
    username = input("Please provide username of the user that you want to update: ")
    user = UserRepository().find_user_by_username(username)
    if not user:
        print(f"User with username = {username} was not found!")
        return

    builder = UserBuilder()
    builder._username = user.username
    update_steps = [
        ("name", builder.name),
        ("email", builder.email),
        ("phone", builder.phone),
        ("age", builder.age)
    ]

    i = 0
    while i < len(update_steps):
        field, setter = update_steps[i]
        try:
          new_value = input(f"{field.upper()}(Leave blank to keep current value): ")
          if new_value.strip() == "":
              new_value = getattr(user, str(field))

          setter(new_value)
          i += 1
        except UserFieldValidationException as e:
            print(e)

    updated_user = builder.build()
    if updated_user:
        UserRepository().update_user(updated_user)
        print("User was updated successfully!")

def delete_user() -> None:
    username = input("Please provide username of the user that you want to delete: ")
    isDeleted = UserRepository().delete_user_by_username(username)
    if isDeleted:
        print(f"User with username = {username} was deleted!")
    else:
       print(f"User with username = {username} was not found!")

def list_all_users() -> None:
    all_users = UserRepository().find_all_users()
    for user in all_users:
        print(user)
