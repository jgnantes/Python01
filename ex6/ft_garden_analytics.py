class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age):
        """Initialize a SecurePlant with name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        else:
            self.name = name
            self._height = height
            self._age = age

    def grow(self, growth=1):
        """Raises a Plant instance's height"""
        if growth < 0:
            print("Growth can't be negative [REJECTED]")
            return
        self._height += growth

    def describe(self):
        """Prints a Plant instance's name and current height"""
        print (f"{self.name}: {self._height}cm")


class FloweringPlant(Plant):
    """Represents a flowering plant in the garden with specific attributes"""
    def __init__(self, name, height, age, color="unknown", blooming=True):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def describe(self):
        """Defines a blooming status and prints a FloweringPlant 
        instance's name, current height, color and blooming status"""
        if self.blooming == True:
            status = "(blooming)"
        else:
            status = "(not blooming)"
        print(f"{self.name}: {self._height}, {self.color} flowers {status}")


if __name__=="__main__":
    Rose = FloweringPlant("Rose", 25, 49, "red", False)
    Rose.describe()
    Rose.grow()
    Rose.describe()
