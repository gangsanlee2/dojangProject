class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = 'abcd'

james = Student()
print(james.school)
print(james.hello)