class Plant:
    """Represents a plant in the garden with basic, secure attributes"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a Plant with name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        self.name = name
        self._height = height
        self._age = age


class Flower(Plant):
    """Represents a flower as a subclass of Plant"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a Flower with Plant attributes as well as color"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Prints a message confirming th flower is blooming"""
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        print(f"{self.name} (Flower): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.color} color")


class Tree(Plant):
    """Represents a tree as a subclass of Plant"""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        """Initialize a Tree with Plant attributes
        as well as trunk diameter (in cm)"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        """Returns a float equivalent to height times trunk diameter (in m²)"""
        return ((self._height / 100) * (self._height / 100) * 3.14)

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade()}", end=' ')
        print("square meters of shade")


class Vegetable(Plant):
    """Represents a Vegetable as a subclass of Plant"""
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        """Initialize a Tree with Plant attributes
        as well as harvest season and nutritional value"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self._height}cm tall,", end=" ")
        print(f"{self._age} days old, {self.harvest_season} harvest")

    def get_nutritional_value(self) -> None:
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    oak = Tree("Oak", 500,  1825,  50)
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
