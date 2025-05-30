from application.users_service import create_user, delete_user, list_all_users, read_user, update_user

OPERATIONS_LIST = """
OPERATIONS LIST:
C -> CREATE USER
R -> READ USER
U -> UPDATE USER
D -> DELETE USER

L -> LIST ALL USERS
E -> EXIT
"""

def start_console_ui():
    is_finished = False
    while not is_finished:
        print(OPERATIONS_LIST)
        choice = input("Provide acronynym of the operation that you want to perform: ")
        match choice:
           case "C" | "c":
               create_user()
           case "R" | "r":
               read_user()
           case "U" | "u":
               update_user()
           case "D" | "d":
               delete_user()
           case "L" | "l":
               list_all_users()
           case "E" | "e":
               return
           case _:
               print("Please provide a valid acronym according to the OPERATIONS LIST")
