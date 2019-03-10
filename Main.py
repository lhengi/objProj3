from Person import Person
from Group import Group

def findPersonById(people,id):
    for i in range(0,len(people)):
        if id == people[i].attribute["id"]:
            return i
    return -1

def findGroupById(groups,id):
    for i in range(0,len(groups)):
        if id == groups[i].id:
            return i
    return -1
def main():

    menu = """
        On -1, end the loop.
        On 0, output what each number does
        On 1, create a new Person. Ask for the first and last name.
        On 2, create a new group, populated by existing Person objects. Loop while outputting the names of people
            who have not been assigned to a group and ask for the ids of the people to add.
        On 3, allow the user to modify an existing group. Ask the user which group they wish to modify. Then ask
            whether they are trying to add or remove members to/from the group. Then, interactively allow the user to add
            or remove as many users as they want by offering a list of available choices and having the user select which
            member to interact with.
        On 4, validate all existing groups, as well as all people to check that they have a group.
        On 5, output each group’s number and members."""

    option = 0
    people = []
    groups = []

    while(option != -1):

        if option == -1:
            print("Goodbye")
            break
        elif option == 0:
            print(menu)
        elif option == 1:
            firstname = input("What's the firstname: ")
            lastname = input("What's the lastname: ")
            newPerson = Person(firstName=firstname,lastName=lastname)
            people.append(newPerson)
        elif option == 2:
            newGroup = Group()
            while True:
                for person in people:
                    if not person.isInGroup():
                        print(person)
                personId = int(input("What's the id of the person you want to add or enter -1 to stop adding: "))
                if personId == -1:
                    break
                personIndex = findPersonById(people,personId)
                newGroup.addPerson(people[personIndex])
                people[personIndex].addGroup(newGroup.id)
            groups.append(newGroup)
        elif option == 3:
            for g in groups:
                print(g)
            groupId = int(input("What's the id of the group you want to modify: "))
            groupIndex = findGroupById(groups,groupId)
            action = input("ADD or REMOVE: ")

            while True:
                if action == "ADD":
                    for person in people:
                        if not person.isInGroup():
                            print(person)
                    personId = int(input("What's the id of the person you want to ADD or enter -1 to stop adding: "))
                    if personId == -1:
                        break
                    personIndex = findPersonById(people, personId)
                    groups[groupIndex].addPerson(personIndex)
                    people[personIndex].addGroup(groups[groupIndex].id)

                elif action == "REMOVE":
                    for person in groups[groupIndex].peopleList:
                        print(person)
                    personId = personId = int(input("What's the id of the person you want to REMOVE or enter -1 to stop adding: "))
                    if personId == -1:
                        break
                    personIndex = findPersonById(people, personId)
                    if personIndex != -1 and groups[groupIndex].removePerson(personId):
                        people[personIndex].removeGroup()
                else:
                    print("IDK what you talking about")
                    break
        elif option == 4:
            validateList = ["firstName", "lastName", "groupNum"]
            for g in groups:
                g.validate(validateList)
            for p in people:
                p.validate(validateList)
        elif option == 5:
            for g in groups:
                g.print()
        else:
            print("No such option, please select again")
        option = int(input("Please Enter an option: "))

main()


