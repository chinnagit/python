from user import User


class EnterpriseUser(User):
    def __init__(self, id, name, managername, managerref):
        User.__init__(id, name)
        self.mangername = managername
        self.managerref = managerref
