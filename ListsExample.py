#List is ordered and can be changeable. Lists are represented in square brackets.

def printList(list):
    if(len(list) > 0):
        for item in list :
         print item

list = ["apple", "banana", 200]
print "Length of list: ", len(list)

print ("print the items in list")

print list

print ("\nprint one item at a time in list")

for item in list :
    print item

list.append(400)

print("\nafter append the list")
printList(list)

list.insert(2, "oranges")

print("\nafter insert in the list")
printList(list)

print("\nafter pop in the list")
list.pop()
printList(list)

print("\nafter delete in the list")
del list[0]
printList(list)

print("\ncheck apple exist in the list")
print("apple" in list)


print("\nafter clear the entire list")
list[:] = []
#list.clear()
printList(list)



print("\nafter delete the entire list")
del list
# printList(list)





