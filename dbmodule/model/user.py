from email import Email


class User:
    # emails = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    # def __init__(self, id, name, emails):
    #     self.id = id
    #     self.name = name
    #     self.emails = emails

    def setemails(self, emails):
        self.emails = emails

    # private function, can not be accessed out side of the class.
    def __somePrivateFunction(self):
        print('accessing private function')


if __name__ == '__main__':
    print('invoking User main method')
    user = User('user-id-1234', 'bala')
    # user.__init__('user-id-1234', 'bala')

    email1 = Email('bala@yahoo.com', 'home', False)
    email2 = Email('bala@symantec.com', 'work', True)
    email3 = Email('bala@gmail.com', 'other', False)
    emails = [email1, email2, email3]

    user.setemails(emails)

    print 'user id: ', user.id, ' name: ', user.name
    for email in user.emails:
        print 'email: ', email.value, ' type: ', email.type, ' is primary: ', email.primary


