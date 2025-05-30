from application.user_builder import FatalUserCreationException, UserBuilder
from application.user_builder import UserFieldValidationException
from storage.user_repository import UserRepository

def create_user() -> None:
    print("You are creating a new user, please provide the following user details")
    while True:
        try:
            user = UserBuilder().username(input("Username:")).name(input("Name:")).email(input("Email:")).phone(input("Phone:")).age(input("Age:")).build()
            if user is None:
                continue
            UserRepository().save_user(user)
            print("User was successfully saved")
            return
        except UserFieldValidationException as e:
            print(e)
        except FatalUserCreationException as e:
            print(e)
            return

def read_user() -> None:
    username = input("Please provide username of the user that you are looking for:")
    user = UserRepository().find_user_by_username(username)
    if user:
        print(f"Found the following user:\n{user}")
    else:
        print(f"User with username = {username} was not found")

def update_user() -> None:
    # TODO: implement this
    return

def delete_user() -> None:
    # TODO: implement this
    return

def list_all_users() -> None:
    # TODO: implement this
    return
