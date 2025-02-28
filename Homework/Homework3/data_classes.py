import json

class Person(object):
    def __init__(self, first, last, age, email):
        self.first = first
        self.last = last
        self.age = age
        self.email = email

class Student(Person):
    def __init__(self, first, last, age, email, ID):
        super().__init__(first, last, age, email)
        self.ID = ID

def save(object, name):
    with open(name, mode="w") as filewrite:
        json.dumps(object), filewrite
        print(json.dumps(object))

#person1 = Student("Bob", "Duncan", 43, "Bob@bobsbugsbegone.com", 245859)
#save(person1, "Bob") //these are all tests