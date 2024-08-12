class Pet():
    def __init__(self , name, age):
        self.n =  name
        self.a = age

    def show(self):
        print(f'hello I am {self.n} a I am {self.a} years old')

class Dog(Pet):
    def __init__(self , name , age , color):
        super().__init__(name ,age)
        self.color = color

    def speak(self):
        print('bark')

class Cat(Pet):
    
    def speak(self):
        print('meow')

p1 = Pet('ssd',21 )
p1.show()
c = Cat('bill' , 14)
c.show()