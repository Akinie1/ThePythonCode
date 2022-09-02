# Classes.
class Planet : 

 def __init__(self):
    self.name = "Akinie Samuel Aterh"
    self.radius = 200000
    self.gravity = 5.5
    self.system = "Hoth System"

 def orbit(self):
    return f"{self.name }"

# creating an instance of the class.
hoth = Planet()
print(f"Name is :  {hoth.name}");
print(f"Radius is : {hoth.radius}");
print(f"Gravity is : {hoth.gravity}");

