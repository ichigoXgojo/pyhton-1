class parrot:

    species = "bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot("Blu", 10)
woo = parrot("Woo", 15) 

print("blu is a {} and is {} years old".format(blu.species, blu.age))
print("woo is a {} and is {} years old".format(woo.species, woo.age))

print("blu is a {} and is {} years old".format(parrot.species, blu.age))    
print("woo is a {} and is {} years old".format(parrot.species, woo.age))