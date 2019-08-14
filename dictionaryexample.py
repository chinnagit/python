# dictionary like hashmap in other languages. unordered, indexed and changeable.

def printDict(dict):
    print("keys alone")
    for key in dict:
        print key
    print("\nvalues alone")
    for value in dict.values():
        print value
    print("\nkeys and values together")
    for key, value in dict.items():
        print(key, value)
    print("\nget specific item from dictionary")
    print(dict["india"])

dictionaryEg = {
    "england": "london",
    "usa": "washington",
    "india": "delhi"
}

printDict(dictionaryEg)

if 'france' in dictionaryEg.keys():
    print "france is exist ", dictionaryEg["france"]
else:
    print ("france is not exist in the list")


