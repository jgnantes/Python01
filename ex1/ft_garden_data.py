class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, days):
        """Initialize a Plant with name, height (cm), and age (days)"""
        self.name = name
        self.height = height
        self.days = days


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)
    print(f"{Rose.name}: {Rose.height}cm, {Rose.days} days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.days} days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.days} days old")
