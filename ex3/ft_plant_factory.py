class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age, growth_rate):
        """Initialize a Plant with name, height (cm), age in days
        and growth_rate (cm/days)"""
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate


def ft_plant_factory(plant_list: list):
    i = 0
    print("=== Plant Factory Output ===")
    for plant in plant_list:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        i += 1
    print("\nTotal plants created:", i)


if __name__ == "__main__":
    plant_list = [
        Plant("Rose", 25, 30, 1),
        Plant("Oak", 200, 365, 0.5),
        Plant("Cactus", 15, 120, 0),
        Plant("Sunflower", 80, 45, 3),
        Plant("Fern", 15, 120, 2),
    ]
    ft_plant_factory(plant_list)
