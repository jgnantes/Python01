class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth_rate: int, days: int):
        for _ in range(days):
            self.height += growth_rate

    def get_older(self, days: int):
        for _ in range(days):
            self.age += 1

    def get_info(self, days: int):
        print(f"=== Day {days + 1} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    Rose = Plant("Rose", 25, 30)
    Rose.get_info(0)
    days = 6
    growth_rate = 1
    Rose.get_older(days)
    Rose.grow(growth_rate, days)
    Rose.get_info(days)
