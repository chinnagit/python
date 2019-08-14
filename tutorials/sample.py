#1.
# weight = input('your weight in pounds: ')
#
# weightInKgms = int(weight) / 2.23
#
# print('Your weight in kgms: '+str(weightInKgms))

#2.
# array = [5, 2, 5, 2, 2]
#
# for val in array:
#     # print "value:", val
#     # i = 0
#     str = ''
#     for i in range(val):
#     # while i < val:
#         # print 'i: ', i
#         str += 'X'
#         # i += 1
#     print str

#3. Find the large number from integer array

# list = [ 10, 5, 100, 250, 4, 3, 75, 150, 500]
#
# large = list[0]
#
# for val in list:
#     if(large < val):
#         large = val
#
# print ('largest of ', list, ' is: '+str(large))

#4. Remove the duplicates from list

# list = [ 10, 5, 100, 250, 4, 3, 75, 150, 500, 5, 5, 100, 500]
# list.sort()
#
# tmp = 99999999
# index = 0
# print ('original list: ', list)
#
# lenList = len(list)
#
# resList = []
#
# # with extra space
# while index < len(list) :
#     # print('value: ' + str(list[index]) + " tmp: " + str(tmp) )
#     if tmp != list[index] :
#         resList.append(list[index])
#         tmp = list[index]
#     index += 1
#
# print ('using while loop', resList)
#
# # no extra space
#
# tmp = 99999
# index = 0
# for i in range(len(list)):
#     if tmp != list[i]:
#         list[index] = list[i]
#         index += 1
#         tmp = list[i]
#
# for i in range(index, len(list)):
#     list[i] = 0
#
# print ('using for loop wiht no extra space', list)

#5. Roll the dice

import random

class Dice:
    # dice = (1, 2, 3, 4, 5, 6)
    # def __init__(self):
    #     print 'in constructor'

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second

dice = Dice()

quit = False

while quit == False:
    quit = input('roll the dice/quit: ')
    if quit == False:
        print ('you rolled: ', dice.roll())
    else:
        print 'quitting'
        break












