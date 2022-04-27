import json
import random
import string


class UserItem:
    """ Models each user Item """

    def __init__(self, email, password):
        self.email = email
        self.password = password


class User:
    """ Models user list and do things with them!"""

    def __init__(self):
        self.users = []
        self.read_again()

    def read_again(self):
        with open("data.txt") as file:
            data = file.read()
            data = data.split("\n")
            for item in data:
                js = json.loads(item)
                self.users.append(js)
            print(self.users)

    def hash_and_add_to_list(self, email, password):
        """Hashes password and writes user to file"""

        split_pass = list(password)
        new_password = ""
        for item in split_pass:
            char = item

            if 64 < ord(item) < 91:
                char = ord(item) + 3
                if char > 90:
                    char = char - 25
                char = chr(char)

            if 96 < ord(item) < 123:
                char = ord(item) + 3
                if char > 122:
                    char = char - 25
                char = chr(char)

            new_password = new_password + char

        my_user = {
            "Email": email,
            "Password": new_password,
        }
        with open("data.txt", "a") as file:
            file.write(f"\n{json.dumps(my_user)}")


    def find_unhash(self, email):
        """Finds by email and unhashes"""
        self.read_again()
        for user in self.users:
            if user["Email"] == email:

                split_pass = list(user["Password"])
                unhashed = ""

                for item in split_pass:
                    char = item

                    if 64 < ord(item) < 91:
                        char = ord(item) - 3
                        if char < 65:
                            char = char + 25
                        char = chr(char)

                    if 96 < ord(item) < 123:
                        char = ord(item) - 3
                        if char < 97:
                            char = char + 25
                        char = chr(char)

                    unhashed = unhashed + char

                return unhashed

    def generate_password(self, option):
        """ Generate random password pf length 12 with letters and symbols or digits"""
        password = ""
        if option == 1:
            characters = string.ascii_letters + string.punctuation
            password = ''.join(random.choice(characters) for i in range(12))
        elif option == 2:
            characters = string.digits
            password = ''.join(random.choice(characters) for i in range(12))
        return password
# https://geekflare.com/password-generator-python-code/



