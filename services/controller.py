from loadprofile import JsonData
from dbmodule.DbMain import DbManager


class Controller:
    def __init__(self):
        print ''

    def createuser(self):
        loaddata = JsonData()
        jsondata = loaddata.getUserData()
        dbManager = DbManager()
        dbManager.createuser(jsondata)


if __name__ == '__main__':
    controller = Controller()
    controller.createuser()
