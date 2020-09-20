def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        email = input("Email: ")


def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    print(name)
    return name




main()