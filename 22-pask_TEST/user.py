import json

class UserItem:
    """ Models each user Item """

    def __init__(self, email, password):
        self.email = email
        self.password = password


class User:
    """ Models user list and do things with them!"""

    def __init__(self):
        self.users = []
        with open("data.txt") as file:
            data = file.read()
            data = data.split("\n")
            print(data)
            for item in data:
                js = json.loads(item)
                self.users.append(js)

        print(self.users)

# https://geekflare.com/password-generator-python-code/



