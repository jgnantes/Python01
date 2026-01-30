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

    def get_info(self):
        print(f"{self.name} (Flower): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.color} color")


class Tree(SecurePlant):
    """Represents a tree as a subclass of SecurePlant"""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a Tree with SecurePlant attributes
        as well as trunk diameter (in cm)"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """Returns a float equivalent to height times trunk diameter (in m²)"""
        return (int(self._height * self.trunk_diameter / 10000))

    def get_info(self):
        print(f"{self.name} (Tree): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade()} square meters of shade")


class Vegetable(SecurePlant):
    """Represents a Vegetable as a subclass of SecurePlant"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a Tree with SecurePlant attributes
        as well as harvest season and nutritional value"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(f"{self.name} (Vegetable): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.harvest_season} harvest")

    def get_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    oak = Tree("Oak", 500, 356, 100)
    elm = Tree("Elm", 2000, 720, 60)
    rose = Flower("Rose", 10, 2, "red")
    marigold = Flower("Marigold", 15, 5, "yellow")
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    bell_pepper = Vegetable("Bell Pepper", 120, 75, "autumn", "antioxidants")
    print("=== Garden Plant Types ===\n")
    print("== Flowers ==")
    rose.get_info()
    rose.bloom()
    marigold.get_info()
    marigold.bloom()
    print("\n")
    print("== Trees ==")
    oak.get_info()
    elm.get_info()
    print("\n")
    print("== Vegetables ==")
    tomato.get_info()
    tomato.get_nutritional_value()
    bell_pepper.get_info()
    bell_pepper.get_nutritional_value()
