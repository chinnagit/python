import json
from dbmodule.model import email as emailModule


class JsonData:
    def __init__(self):
        print("")

    def getUserData(self):
        file = open("userprofile.json", "r")
        allData = ""
        for line in file:
            allData += line
        return json.loads(allData)


if __name__ == '__main__':
    data = JsonData()
    jsonData = data.getUserData()
    print(jsonData["userName"])
    print(json.dumps(jsonData, indent=2))
    emails = jsonData["emails"]
    print(emails)
    for email in emails:
        em = emailModule.Email(email["value"], email["type"], email["primary"])
        print(email["type"])
        print(email["primary"])
        print(email["value"])

        print(em.type)
        print(em.primary)
        print(em.value)


