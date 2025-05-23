# You are asked to model an application for storing data about people. You should be able to have a Person and a Child. Every person receives name and age upon initialization. Your task is to model the application.
# Create a Child class that inherits a Person and has the same constructor definition. However, do not copy the code from the Person class - reuse the Person class's constructor.
# Submit in judge a zip file named project, containing a separate file (person.py and child.py) for each of the classes.

from project.person import Person
from project.child import Child
# test
person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)

# output
# Peter
# 25
# Person