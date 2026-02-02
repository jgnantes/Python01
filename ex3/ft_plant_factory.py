class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age):
        """Initializes a Plant with name, height (cm), age in days"""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(data: list) -> int:
    """Prints the basic information of every Plant object from a list
    and returns the amount of created objects"""
    print("=== Plant Factory Output ===")
    i = 0
    for p in data:
        plant = Plant(p[0], p[1], p[2])
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        i += 1
    return i


if __name__ == "__main__":
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 15, 120),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    n = ft_plant_factory(data)
    print("\nTotal plants created:", n)
