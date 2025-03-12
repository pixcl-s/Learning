# Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str). Implement the
# needed magic methods so that:
#   • Each person could be represented by their names, separated by a single space.
#   • When you concatenate two people, you should return a new instance of a person who will take the first
#       name from the first person and the surname from the second person.
# Create another class called Group. Upon initialization, it should receive a name (str) and people (list of Person
# instances). Implement the needed magic methods so that:
#   • When you access the length of a group instance, you should receive the total number of people in the group.
#   • When you concatenate two groups, you should return a new instance of a group which will have a name
#       string in the format "{first_name} {second_name}" and all the people in the two groups will participate in the new one too.
#   • Each group should be represented in the format "Group {name} with members {members' names separated by comma and space}"
#   • You could iterate over a group, and each person (element of the group) should be represented in the format "Person {index}: {person's name}"

from typing import List


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person") -> "Person":
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]):
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other: "Group") -> "Group":
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(f'{x.name} {x.surname}' for x in self.people)}"

    def __iter__(self) -> str:
        for x, y in enumerate(self.people):
            yield f"Person {x}: {str(y)}"

    def __getitem__(self, item: int) -> str:
        return f"Person {item}: {str(self.people[item])}"


# 100/100
# test
p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)
# output
# 3
# Group Special with members Elon Musk, Warren Musk
# Person 0: Aliko Dangote
# Person 0: Aliko Dangote
# Person 1: Bill Gates
# Person 2: Warren Buffet
# Person 3: Elon Musk
# Person 4: Warren Musk

# import unittest
#
#
# class TestGroups(unittest.TestCase):
#     def setUp(self):
#         self.p0 = Person('Aliko', 'Dangote')
#         self.p1 = Person('Bill', 'Gates')
#         self.p2 = Person('Warren', 'Buffet')
#         self.p3 = Person('Elon', 'Musk')
#
#     def test_person_init(self):
#         self.assertEqual(self.p0.name, 'Aliko')
#         self.assertEqual(self.p0.surname, 'Dangote')
#
#     def test_person_str(self):
#         self.assertEqual(str(self.p1), 'Bill Gates')
#
#     def test_person_add(self):
#         self.assertEqual(str(self.p2 + self.p3), 'Warren Musk')
#
#     def test_group_init(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(first_group.name, '__VIP__')
#         self.assertEqual(first_group.people, [self.p0, self.p1, self.p2])
#
#     def test_group_str(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(str(first_group), "Group __VIP__ with members Aliko Dangote, Bill Gates, Warren Buffet")
#
#     def test_group_len(self):
#         first_group = Group('__VIP__', [self.p0, self.p1, self.p2])
#         self.assertEqual(len(first_group), 3)
#
#
# if __name__ == "__main__":
#     unittest.main()