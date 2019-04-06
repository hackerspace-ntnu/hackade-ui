"""
Her kommer div globale og overordnede ting som bør defineres
"""

import libs.utils as utils


class HackadeState:

    def __init__(self, user_base="defaults/defaultUsers.json", user="guest"):

        userDict: dict = utils.jsonLoad(user_base)

        self.activeUser = self.userDict[user]

        self.activePlugin = "none"

    @property
    def user(self):
        return self.user

    @user.setter
    def user(self, new_user: str):
        if new_user not in self.userDict.keys():
            raise ValueError("New user {} not in current list of users {}.".format(new_user, self.userDict.keys()))

        self.activeUser = new_user

    def change_pluggin(self, new_pluggin_name):
        pass
