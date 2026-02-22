class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes a Plant with name, height (cm), age in days"""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(data: list) -> tuple:
    """Prints the basic information of every Plant object from a list
    and returns the amount of created objects"""
    i: int = 0
    plant_list: list = []
    for p in data:
        plant = Plant(p[0], p[1], p[2])
        plant_list += [plant]
        i += 1
    return i, plant_list


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    n, plant_list = ft_plant_factory(data)
    for plant in plant_list:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
    print("\nTotal plants created:", n)
