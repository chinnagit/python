# set is un ordered and unindexed, written in curly brackets.

def printSet(set):
    for item in set:
        print item

seteg = {"apple", "banana", 200}

printSet(seteg)

# print("access by index not supported")
# print seteg[1]

print("\nadd item to set")
seteg.add(300)
printSet(seteg)

print("\nadd multiple items at once")
seteg.update(["oranges", "tomotoes", 500])
printSet(seteg)

