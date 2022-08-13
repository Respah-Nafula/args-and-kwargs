from unicodedata import name


class Dog:
    species="carnis familiaris"
    def __init__(self,name,age,colour):
        self.name=name
        self.age=age
        self.colour=colour
        
        #  instance method
    def description(self):
     return f"{self.colour} {self.name} is {self.age} years old"

    def barking(self,sound):
     return f"{self.name} barks{sound}"
                
#     Create a Car class with two instance attributes:

# .color, which stores the name of the car’s color as a string
# .mileage, which stores the number of miles on the car as an integer
# Then instantiate two Car objects—a blue car with 20,000 miles and a red car with 30,000 miles—and print out their colors and mileage. Your output should look like this:

# The blue car has 20,000 miles.
# The red car has 30,000 miles.

class Car():
    def __init__(self, name, mileage):
       self.name=name
       self.mileage=mileage
       

    def vehicle(self):
            return f"The {self.name}  car has{self.mileage}"

    def vehicle1(self):
                return f"The {self.name} car has {self.mileage}"