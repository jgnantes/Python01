class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    growth = 6

    def grow(Plant, growth):
        Plant.height += growth

    def age(Plant):
        Plant.age = Plant.age + 6

    print("=== Day 1 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    grow(Rose, growth)
    age(Rose)
    print("=== Day 7 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    print(f"Growth this week: +{growth}cm")
