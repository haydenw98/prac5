def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = (input("Is your name {}?".format(name)).upper())

        if confirm != 'Y' and confirm != '':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for k, v in email_to_name.items():
        print("{} ({})".format(v, k))


def get_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    print(name)
    return name




main()