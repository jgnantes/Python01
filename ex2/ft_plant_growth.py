class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def grow(self, growth):
        self.height += growth
    def age_week(self):
        self.age += 6

if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    growth = 6
    print("=== Day 1 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    Rose.grow(growth)
    Rose.age_week()
    print("=== Day 7 ===")
    print(f"{Rose.name}: {Rose.height}cm, {Rose.age} days old")
    print(f"Growth this week: +{growth}cm")
