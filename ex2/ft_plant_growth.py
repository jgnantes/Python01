class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, days, growth_rate):
        """Initialize a Plant with name, height (cm), age in days
        and growth_rate in cm/days"""
        self.name = name
        self.height = height
        self.days = days
        self.growth_rate = growth_rate

    def age(self, time_passed: int):
        """Changes a Plant instance's age based on time passed in days"""
        for _ in range(time_passed):
            self.days += 1

    def grow(self, time_passed: int):
        """Changes a Plant instance's height based on a given
        growth rate (cm/day) and time_passed passed in days"""
        for _ in range(time_passed):
            self.height += self.growth_rate

    def get_info(self):
        """Prints information about a Plant instance"""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30, 1)
    Sunflower = Plant("Sunflower", 80, 45, 3)
    Cactus = Plant("Cactus", 15, 120, 0)
    print("=== Day 1 ===")
    Rose.get_info()
    Sunflower.get_info()
    Cactus.get_info()
    time_passed = 6
    Rose.age(time_passed)
    Rose.grow(time_passed)
    Sunflower.age(time_passed)
    Sunflower.grow(time_passed)
    Cactus.age(time_passed)
    Cactus.grow(time_passed)
    print(f"=== Day {time_passed + 1} ===")
    Rose.get_info()
    Sunflower.get_info()
    Cactus.get_info()
