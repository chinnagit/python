class Iterator:

    def __init__(self, list):
        self.list = list
        # __index will be treated as private variable of class
        self.__index = 0

    def haxnext(self):
        if self.__index < len(list):
            return True
        else:
            return False

    def next(self):
        value = list[self.__index]
        self.__index += 1
        return value


if __name__ == '__main__':
    print('Iterator implementation')
    list = [10, 20, 30, 40, 50]
    iter = Iterator(list)

    while iter.haxnext() :
        # print("index value: ", iter.__index)
        iter._somePrivateFunction()
        print iter.next()
