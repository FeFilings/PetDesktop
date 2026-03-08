import OtherLibrary

# Tracking the number of pets
petCount = 0

def GetPetCount():
    # Get the pet count from a file on the desktop called pet_count.txt
    # Write 0 to the file and return 0 if the file does not exist yet
    try:
        with open("C:/Users/roger/OneDrive/Desktop/pet_count.txt", "r") as funky:
            count = int(funky.read())
            return count
    except FileNotFoundError:
        with open("C:/Users/roger/OneDrive/Desktop/pet_count.txt", "w") as funky:
            funky.write("0")
        return 0

def AddPet():
    count = GetPetCount()
    count += 1
    with open("C:/Users/roger/OneDrive/Desktop/pet_count.txt", "w") as funky:
        funky.write(str(count))
    
if __name__ == "__main__":
    GetPetCount()
    print(GetPetCount())