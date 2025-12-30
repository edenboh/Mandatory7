#ex1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

bengal1=Bengal("loulou",10)
chartreux1=Chartreux("chouchou",5)
siamese1=Siamese("doudou",2)
all_cats = [bengal1, chartreux1, siamese1]
sara_pets=Pets(all_cats)
sara_pets.walk()

#ex2
class Dog:
    def __init__(self, name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return (f"{self.name} is barking.")

    def run_speed(self):
        return ((self.weight / self.age) * 10)

    def fight(self, other_dog):
        myForce=self.run_speed()*self.weight
        otherDogForce=other_dog.run_speed()*other_dog.weight
        if(myForce>otherDogForce):
            return(f"{self.name } has won")
        else:
            return(f"{other_dog.name } has won")
# Step 2: Create dog instances
dog1=Dog("loulou",10,15)
dog2=Dog("chouchou",5,16)
dog3=Dog("doudou",2,12)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))

#exo4
class Person:
    def __init__(self,first_name,age,last_name=" "):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def is_18(self):
        if (self.age>18):
            return True
        return False

class Family:
    def __init__(self,last_name):
        self.last_name=last_name
        self.members=[]
    def born(self,first_name, age):
        p1=Person(first_name,age,self.last_name)
        self.members.append(p1)

    def check_majority(self,first_name):
        sentence=""
        for person in self.members:
            if person.first_name == first_name:
                if(person.is_18()):
                    sentence="You are over 18, your parents Jane and John accept that you will go out with your friends"
                else:
                    sentence="Sorry, you are not allowed to go out with your friends."
            
            
        print(sentence) 
    
   

            
    def family_presentation(self):
        print(self.last_name)
        for person in self.members:
            print(f"{person.first_name} has {person.age}")

f1=Family("BOHBOT")
f1.born("Eden",22)
f1.born("David",25)
f1.born("Nathan",28)
f1.born("Jade",17)
f1.check_majority("Jade")
f1.check_majority("Nathan")
f1.family_presentation()

            

