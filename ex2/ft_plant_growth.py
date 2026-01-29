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

    def grow_older(self, time_passed: int):
        self.age(time_passed)
        self.grow(time_passed)

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
    Rose.grow_older(time_passed)
    Sunflower.grow_older(time_passed)
    Cactus.grow_older(time_passed)
    print(f"=== Day {time_passed + 1} ===")
    Rose.get_info()
    Sunflower.get_info()
    Cactus.get_info()
