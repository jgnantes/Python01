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

    def grow(self, time_passed: int) -> int:
        """Changes a Plant instance's height based on its
        growth rate in cm/day and time passed passed in days"""
        growth = 0
        for _ in range(time_passed):
            growth += self.growth_rate
        self.height += growth
        return growth

    def grow_older(self, time_passed: int) -> int:
        self.age(time_passed)
        growth = self.grow(time_passed)
        return growth

    def get_info(self):
        """Prints information about a Plant instance"""
        print(f"{self.name}: {self.height}cm, {self.age_a} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 49)
    Sunflower = Plant("Sunflower", 75, 24)
    Cactus = Plant("Cactus", 50, 49)
    print("=== Day 1 ===")
    Rose.get_info()
    Sunflower.get_info()
    Cactus.get_info()
    time_passed = 6
    growth_rose = Rose.grow_older(time_passed)
    growth_sunflower = Sunflower.grow_older(time_passed)
    growth_cactus = Cactus.grow_older(time_passed)
    print(f"=== Day {time_passed + 1} ===")
    Rose.get_info()
    print(f"Growth this week: {growth_rose}")
    Sunflower.get_info()
    print(f"Growth this week: {growth_sunflower}")
    Cactus.get_info()
    print(f"Growth this week: {growth_cactus}")
