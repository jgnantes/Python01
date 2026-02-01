class Plant:
    """Represents a plant in the garden with basic attributes"""
    def __init__(self, name, height, age):
        """Initialize a Plant instance with
        name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        else:
            self.name = name
            self._height = height
            self._age = age

    def grow(self, growth=1) -> int:
        """Raises a Plant instance's height"""
        if growth < 0:
            print("Growth can't be negative [REJECTED]")
            return
        self._height += growth
        return growth

    def describe(self):
        """Prints a Plant instance's name and current height"""
        print(f"{self.name}: {self._height}cm")


class FloweringPlant(Plant):
    """Represents a flowering plant in the garden with specific attributes"""
    def __init__(
        self,
        name,
        height,
        age,
        color="unknown",
        blooming=True
    ):
        """Initialize a FloweringPlant instance with all Plant attributes
        as well as color and a booleans for blooming status"""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def describe(self):
        """Defines a blooming status and prints a FloweringPlant
        instance's name, current height, color and blooming status"""
        if self.blooming is True:
            status = "(blooming)"
        else:
            status = "(not blooming)"
        print(f"{self.name}: {self._height}, {self.color} flowers {status}")


class PrizeFlower(FloweringPlant):
    """Represents a prize flower in the garden with specific attributes"""
    def __init__(
        self,
        name,
        height,
        age,
        color="unknown",
        blooming=True,
        prize_points=0
    ):
        """Initialize a PrizeFlower instance with all FloweringPlant attributes
        as well as prize points"""
        super().__init__(name, height, age, color, blooming)
        self.prize_points = prize_points

    def describe(self):
        """Defines a blooming status and prints a FloweringPlant
        instance's name, current height, color and blooming status"""
        if self.blooming is True:
            status = "(blooming)"
        else:
            status = "(not blooming)"
        print(f"{self.name}: {self._height}, {self.color} flowers {status}")
        print(f"Prize Points: {self.prize_points}")


class GardenManager:
    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0

        def record_add(self):
            self.plants_added += 1

        def record_growth(self, growth):
            self.total_growth += growth

        def count_types(self, plants):
            regular = 0
            flowering = 0
            prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    class Garden:
        def __init__(self, owner):
            self.owner = owner
            self.plant_list = []
            self.stats = GardenManager.GardenStats()

        def add_plant(self, plant):
            self.plan_list.append(plant)
            self.stats.record_add()

        def help_all_grow(self, growth=1):
            print(f"{self.owner} is hellping all plants grow")
            for p in self.plants:
                size_result = p.grow(growth)
                self.stats.record_growth(size_result)
                print(f"{p.name} grew {size_result}cm")


if __name__ == "__main__":
    Rose = PrizeFlower("Rose", 25, 49, "red", False, 80)
    Rose.describe()
    Rose.grow()
    Rose.describe()
