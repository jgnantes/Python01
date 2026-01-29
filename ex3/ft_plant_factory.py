class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age):
        """Initialize a Plant with name, height (cm), age in days"""
        self.name = name
        self.height = height
        self.age = age


def ft_plant_factory(plant_list: list) -> int:
    """Prints the basic informaion of every Plant object from a list
    and returns the amount of created objects"""
    i = 0
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        i += 1
    return i


if __name__ == "__main__":
    plant_list = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]
    i = ft_plant_factory(plant_list)
    print("\nTotal plants created:", i)
