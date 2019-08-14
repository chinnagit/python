#tuples are oredered and unchangeable. Tuples are stroed as in normal brackets ()

def printTuple(tuple):
    for item in tuple:
        print item

items = ("apple", "banana", 200)

print(items)

print("\none item at a time")
printTuple(items)

items[2] = "oranges"



