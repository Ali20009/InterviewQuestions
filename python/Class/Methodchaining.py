class Car:
    def turn_on(self):
        print('this car is turned on')
        return self  # Because if yot do not return any thing it returns None
    
    def drive(self):
        print('this car is driving')
        return self
    
    def brak(self):
        print('you step on the breaks')
        return self
    
    def turn_off(self):
        print('you turned the car off')
        
    
car = Car()
print(car.turn_on()
      .drive()
      .brak()
      .turn_off())