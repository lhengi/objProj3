
class Group(object):
    numGroup = 0

    def __init__(self):
        Group.numGroup += 1

        self.id = Group.numGroup

        self.peopleList = []

    def addPerson(self,person):
        person.addGroup(self.id)
        self.peopleList.append(person)

    def removePerson(self,personId):
        index = -1
        for i in range(0,self.peopleList):
            if personId == self.peopleList[i].attribute["id"]:
                index = i
                break
        if index == -1:
            print("can't find Person ",personId)
            return False
        self.peopleList.pop(index)
        return True



    def validate(self,keys):
        for person in self.peopleList:
            person.validate(keys)

    def print(self):
        print("Group Id: ",self.id," Total memebers: ",len(self.peopleList))
        for person in self.peopleList:
            print(person)
    def __str__(self):
        return "Group"+str(self.id)