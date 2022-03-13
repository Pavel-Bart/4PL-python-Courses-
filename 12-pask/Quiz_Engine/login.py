
class UserItem:

    def __init__(self, username, password, highscore):
        self.username = username,
        self.password = password
        self.highscore = highscore


class Login:

    def __init__(self):
        self.users = []

        with open("login.txt") as file:
            user_list = file.readlines()

        for item in user_list:
            user_data = item.split()
            print(user_data)
            self.users.append(UserItem(username=user_data[0], password=user_data[1], highscore=user_data[2]))

    def Check_log(self, username, password):
        for item in self.users:
            print(type(item.username))
            if str(item.username) == username and item.password == password:
                return item

        print("Incorrect username or password!")
        return None
