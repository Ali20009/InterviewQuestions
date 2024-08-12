
class Person:
    number_of_people = 0

    def __init__(self , name):
        self.names = []
        Person.add()

    @classmethod
    def number(cls):
        return cls.number_of_people
    
    @classmethod
    def add(cls):
        cls.number_of_people += 1
    
 
p1 = Person('Bob')
p2 = Person('Michle')

print(Person.number())