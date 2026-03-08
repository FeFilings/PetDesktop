# Tracking the number of pets
pets = []

# Pet classes
class Pet:
    def __init__(self, name, species): 
        self.name = name
        self.species = species

    def MakeNoise(self):
        return "I'm a pet and I make noise!"
    
    def GetRepresentation(self):
        return f"{self.name} {self.species}"
    
class Turtle(Pet):
    def __init__(self, name):
        super().__init__(name, "Turtle")

    def MakeNoise(self):
        return "I'm a turtle and I make noise!"

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def MakeNoise(self):
        return "Woof!"

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def MakeNoise(self):
        return "Meow!"

class Fish(Pet):
    def __init__(self, name):
        super().__init__(name, "Fish")

    def MakeNoise(self):
        return "Blub blub!"

class Bird(Pet):
    def __init__(self, name):
        super().__init__(name, "Bird")

    def MakeNoise(self):
        return "Tweet!"


def LoadPets():
    # Get the pet count from a file on the desktop called pet_count.txt
    # Write 0 to the file and return 0 if the file does not exist yet
    global pets
    try:
        with open("C:/Users/roger/OneDrive/Desktop/pets.txt", "r") as petFile:
            # loop over files lines and create pet objects
            for line in petFile:
                name, species = line.strip().split(" ")
                pets.append(GetPetFromSpecies(name, species))
            
    except FileNotFoundError:
        SavePets()

def SavePets():
    global pets
    with open("C:/Users/roger/OneDrive/Desktop/pets.txt", "w") as petFile:
        for pet in pets:
            petFile.write(f"{pet.GetRepresentation()}\n")

def GetPetFromSpecies(name, species):
    newPet = None
    match species:
        case "Turtle":
            newPet = Turtle(name)
        case "Dog":
            newPet = Dog(name)
        case "Cat":
            newPet = Cat(name)
        case "Fish":
            newPet = Fish(name)
        case "Bird":
            newPet = Bird(name)
        case _:
            newPet = Pet(name, species)
    return newPet

def AddPet(name, species):
    global pets
    pets.append(GetPetFromSpecies(name, species))

def RemovePet(name):
    global pets
    for pet in pets:
        if (pet.name == name):
            pets.remove(pet)
            break

def DisplayPets():
    global pets
    print("Pets:")
    for pet in pets:
        print(f"\t{pet.name} the {pet.species} -> {pet.MakeNoise()}")
    
if __name__ == "__main__":
    LoadPets()

    DisplayPets()
    AddPet("Carl", "Walrus")

    DisplayPets()
    SavePets()