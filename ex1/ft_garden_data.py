class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    print(f"{Sunflower.name}: {Sunflower.height}cm, {Sunflower.age} days old")
    print(f"{Cactus.name}: {Cactus.height}cm, {Cactus.age} days old")
