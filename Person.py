
"""
Author: Heng Li


Create a Person class in a file named Person.py.
The person class should contain a class variable storing the
number of person objects that have been created so far to provide a default value for id in the constructor.

Person objects have a variety of potential attributes, so instead of enumerating all of them as instance variables,
the Person class should have a single instance variable which is a dictionary called attributes.
Each descriptor will have a key of the string attribute name, which means you will perform lookups
with obj.attribute[“attrName”] instead of obj.attrName.

The Person class should have constructors that allow for no parameters, an id, a name, and a dictionary of attributes.
Note that Python only supports a single __init__ function, if you write multiple the last one will override the __init__
function pointer. The Person class should also have a function validate which takes a list of attributes and outputs a line
for each attribute missing. If no attributes are provided, validate should check that the person is assigned to a group.
Examples are given in the sample output.

"""

import copy

class Person(object):
    population = 0

    def __init__(self, firstName=None,lastName=None, id=None,attr=None):
        Person.population += 1
        self.attribute = copy.deepcopy(attr) if attr is not None else {}
        if id is not None:
            self.attribute["id"] = id
        elif not "id" in self.attribute or self.attribute["id"] is None:
            self.attribute["id"] = Person.population

        if firstName is not None:
            self.attribute["firstName"] = firstName
        elif not "firstName" in self.attribute:
            self.attribute["firstName"] = None

        if lastName is not None:
            self.attribute["lastName"] = lastName
        elif not "lastName" in self.attribute:
            self.attribute["lastName"] = None

        self.attribute["groupNum"] = None

    def validate(self,keys=None):
        if keys is None or len(keys) == 0:
            if self.attribute["groupNum"] is None:
                print(self.attribute["firstName"]," ",self.attribute["lastName"], " Doesn't have a group")
            return

        for key in keys:
            if not key in keys or self.attribute[key] is None:
                print(self.attribute["firstName"]," ",self.attribute["lastName"]," Doesn't have a ",key)

    def isInGroup(self):
        return self.attribute["groupNum"] is not None

    def addGroup(self,groupId):
        if self.attribute["groupNum"] is None:
            self.attribute["groupNum"] = groupId
            return
        print("Person ",self.attribute["id"]," is already in a group, Please remove first!")

    def removeGroup(self):
        self.attribute["groupNum"] = None

    def getFullName(self):
        return self.attribute["firstName"]+" "+self.attribute["lastName"]

    def __str__(self):
        return str(self.attribute["id"]) + " " + self.attribute["firstName"] + " " + self.attribute["lastName"]
