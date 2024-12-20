#Specialization

class Vehicle:
  def __init__(self,brand,speed):
    self.brand=brand
    self.speed=speed
    
  def drive(self):
    print(f"The {self.brand} vehicle drives at {self.speed} km/h")
    
class Car(Vehicle):
  def __init__(self,brand,speed,seats):
    super().__init__(brand,speed)
    self.seats=seats
    
  def drive(self):
    print(f"The {self.brand} car drives at {self.speed} km/h which has {self.seats}")
    
vehicle=Vehicle("Generic",100)
car=Car("Toyota",150,5)
vehicle.drive()
car.drive()
    
    
#dependency

class Payment:
  def __init__(self,amount):
    self.amount=amount
    
  def process_payment(self):
    print(f"Processing payment of ${self.amount}")
    
class Order:
  def  __init__(self,order_id,amount):
    self.order_id=order_id
    self.amount=amount
  
  def place_order(self):
    print(f"Placing order #{self.order_id}")
    payment=Payment(self.amount)
    payment.process_payment()
    
order = Order(101,250.50)
order.place_order()
  
  
  
    
    
#Realization

from abc import ABC, abstractmethod

class Animal(ABC): #Abstract Class (interface)
  @abstractmethod
  def sound(self):
    pass
  
  @abstractmethod
  def move(self):
    pass
  
class Dog(Animal): #Realization
  def sound(self):
    return "Bark"
    
  def move(self):
    return "run"
    
dog=Dog()
print(dog.sound())
print(dog.move())







#Generalization and Specialiuzation

class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    
  def work(self):
    print(f"{self.name} is working")
    
class Manager(Employee): #Specialiuzation
  def __init__(self,name,salary,department):
    super().__init__(name,salary)
    self.department=department
    
  def manage(self):
    print(f"{self.name} is managing the {self.department} department")
    
class Intern(Employee): #Specialiuzation
  def __init__(self,name,salary,mentor):
    super().__init__(name,salary)
    self.mentor=mentor
    
  def learn(self):
    print(f"The intern {self.name} is learning from the mentor {self.mentor}")
    
   #Generalization and Specialiuzation 
manager=Manager("Prakash",40000,"hr")
intern = Intern("mohit",9000,"Prakash")

manager.work()
manager.manage()
intern.work()
intern.learn()

  













