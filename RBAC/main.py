import casbin


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def create_user():
        name = input("Name:\n> ")
        name = name.lower()
        name = name.strip()
        role = None
        while role not in {"1", "2", "professor", "student", "Professor", "Student"}:
            role = input("Role:\n1. Professor\n2. Student\n> ")
        if role == "1" or role == "Professor":
            role = "professor"
        if role == "2" or role == "Student":
            role = "student"
        new_user = User(name, role)
        with open("policy.csv", "a") as csv_file:
            csv_file.write(f"g, {new_user.name}, {new_user.role}\n")

    def show_permissions(user):
        enforcer = casbin.Enforcer("./model.conf", "./policy.csv")

        sub = user.strip()
        obj = "data"
        read = "read"
        write = "write"

        if enforcer.enforce(sub, obj, write):
            print("This user has the following permissions: read, write")
        elif enforcer.enforce(sub, obj, read):
            print("This user has the following permissions: read")


def menu():
    print("=== MENU ===")
    print("1. Create a new user")
    print("2. Show user permissions")
    option = None
    while option not in {"1", "2"}:
        option = input("> ")

    match option:
        case "1":
            User.create_user()
        case "2":
            user = input(
                "Type the name of the user you want to see the permissions:\n> "
            )
            User.show_permissions(user)


if __name__ == "__main__":

    menu()
