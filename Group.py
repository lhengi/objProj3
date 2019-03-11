
class Group(object):
    numGroup = 0

    def __init__(self):
        Group.numGroup += 1

        self.id = Group.numGroup

        self.peopleList = []

    def addPerson(self,person):
        person.addGroup(self.id)
        self.peopleList.append(person)

    def removePerson(self,index):
        if index < 0 or index >= len(self.peopleList):
            return False
        self.peopleList.pop(index)
        return True



    def validate(self,keys):
        print()
        if len(self.peopleList) < 3:
            print("Group ",self.id," Has ",len(self.peopleList),"People, Less than three people")
        elif len(self.peopleList) > 5:
            print("Group ", self.id, " Has ", len(self.peopleList), "People, More than five people")

        for person in self.peopleList:
            person.validate(keys)

    def print(self):
        print("Group Id: ",self.id," Total memebers: ",len(self.peopleList))
        for person in self.peopleList:
            print(person)
    def __str__(self):
        return "Group"+str(self.id)