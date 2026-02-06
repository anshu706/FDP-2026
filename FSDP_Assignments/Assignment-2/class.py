class Dog:
    species = "GGolden Retriever"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


print(Dog.species)  # Accessing class attribute
