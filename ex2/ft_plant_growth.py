class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age_a):
        """Initializes a Plant with name, height (cm), age in days
        and growth_rate in cm/day"""
        self.name = name
        self.height = height
        self.age_a = age_a
        self.growth_rate = height / (age_a + 1)

    def age(self, time_passed: int):
        """Changes a Plant instance's age based on time passed in days"""
        for _ in range(time_passed):
            self.age_a += 1

    def grow(self, time_passed: int):
        """Changes a Plant instance's height based on its
        growth rate in cm/day and time passed passed in days"""
        for _ in range(time_passed):
            self.height += self.growth_rate

    def grow_older(self, time_passed: int):
        self.age(time_passed)
        self.grow(time_passed)

    def get_info(self):
        """Prints information about a Plant instance"""
        height_int = int(self.height)
        print(f"{self.name}: {height_int}cm, {self.age_a} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)
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
