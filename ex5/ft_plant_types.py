class SecurePlant:
    """Represents a plant in the garden with basic, secure attributes"""
    def __init__(self, name, height, age):
        """Initialize a SecurePlant with name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        self.name = name
        self._height = height
        self._age = age


class Flower(SecurePlant):
    """Represents a flower as a subclass of SecurePlant"""
    def __init__(self, name, height, age, color):
        """Initialize a Flower with SecurePlant attributes as well as color"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Prints a message confirming th flower is blooming"""
        print(f"{self.name} is blooming beautifully!")


class Tree(SecurePlant):
    """Represents a tree as a subclass of SecurePlant"""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a Tree with SecurePlant attributes as well as trunk diameter (in cm)"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    
    def produce_shade(self):
        """Returns a float equivalent to height * diameter in m²"""
        return (self._height * self.trunk_diameter / 100)


class Vegetable(SecurePlant):
    """Represents a vegetable as a subclass of SecurePlant"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a Tree with SecurePlant attributes 
        as well as harvest season and nutritional value"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__=="__main__":
    oak = Tree("Oak", 200, 356, 5)
    print(f"{oak.name} provides {oak.produce_shade()} square meters of shade\n")
    rose = Flower("Rose", 10, 2, "red")
    print(f"{rose.name} is a {rose.color} flower")
    rose.bloom()
