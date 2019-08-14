# name = raw_input('what is your name? ')
# color = raw_input('what is your favorite color ')
#
# print('Hi '+name + ' likes ' + color)

# weight = raw_input('what is your weight in pound? ')
# weight_in_kgs = float(weight)/2.25
# print('{name} weight is ' + str(weight_in_kgs))
#
# name = 'jayanth'
#
# print(name[-3:])


# is_good = False
#
# if is_good :
#     print("pay 10 % down payment")
#
# else :
#     print("pay 20 % down payment")

numbers = [10, 5, 25, 40, 20, 30]

maxNumber = 0

for number in numbers:
    if number > maxNumber :
        maxNumber = number

print("Max number: "+str(maxNumber))
