"""
Her kommer div globale og overordnede ting som bør defineres
"""


class HackadeState:

    def __init__(self, user="guest", plugin="none", userBase="defaultUsers.json"):
        self.activeUser = user
        self.activePlugin = plugin

        self.userList = list()

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, newUser):
        if newUser not in self.userList:
            raise ValueError("New user {} not in current list of users {}.".format(newUser, self.userList))

        self.activeUser = newUser
