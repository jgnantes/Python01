class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age):
        """Initializes a Plant with name, height (cm), age in days"""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(plant_list: list) -> int:
    """Prints the basic information of every Plant object from a list
    and returns the amount of created objects"""
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    return len(plant_list)


if __name__ == "__main__":
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 15, 120),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    plant_list = [Plant(*p) for p in data]
    n = ft_plant_factory(plant_list)
    print("\nTotal plants created:", n)
