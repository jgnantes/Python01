class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, days):
        """Initialize a Plant with name, height (cm), and age in days"""
        self.name = name
        self.height = height
        self.days = days

    def age(self, time_passed: int):
        """Changes a Plant instance's age based on time passed in days"""
        for _ in range(days):
            self.days += 1

    def grow(self, growth_rate: int, time_passed: int):
        """Changes a Plant instance's height based on a given
        growth rate (cm/day) and time_passed passed in days"""
        for _ in range(days):
            self.height += growth_rate

    def get_info(self, days: int):
        """Prints information about a Plant instance"""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)
    print("=== Day 1 ===")
    Rose.get_info(0)
    Sunflower.get_info(0)
    Cactus.get_info(0)
    days = 6
    growth_rate = 1
    Rose.age(days)
    Rose.grow(growth_rate, days)
    growth_rate = 3
    Sunflower.age(days)
    Sunflower.grow(growth_rate, days)
    growth_rate = 0
    Cactus.age(days)
    Cactus.grow(growth_rate, days)
    print(f"=== Day {days + 1} ===")
    Rose.get_info(days)
    Sunflower.get_info(days)
    Cactus.get_info(days)
