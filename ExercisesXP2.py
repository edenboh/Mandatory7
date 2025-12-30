#exo3
from ExercisesXP  import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__( name, age, weight)
        self.trained=False
    
    def train(self):
        print(self.bark())
        self.trained=True

    def play(self, *dogs):
        dogNames = self.name + " "
        for dog in dogs:
            dogNames += dog.name + " "
        print(f"{dogNames}all play together")
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        myRandom=random.randint(1, 4)
        if(self.trained==True):
            print(tricks[myRandom])
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
buddy = PetDog("Buddy", 3, 12)
max_dog = PetDog("Max", 4, 15)

my_dog.play(buddy, max_dog)
my_dog.do_a_trick()


