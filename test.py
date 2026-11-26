
class Animals:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def sleep(self):
        print(f"{self.name} is sleeping")

    def eat(self):
        print(f"{self.name} is eating")

animal1=Animals("kari", 12)

animal1.sleep() 

print(animal1.name)
print(animal1.age)
print(animal1.__dict__)


class Cat(Animals):
        def __init__(self, name, age, race):
             super().__init__(name, age)
             self.race = race




cat1=Cat("1",1, "1" )

print(cat1.race)

cat1.sleep()






from phone import Phone



phone1= Phone("Iphone 12", 512, 'Desert Rose')
phone2= Phone("Samsung Z fold", 512, "black")

print(Phone.num)

print(phone1.__dict__)