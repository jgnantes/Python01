class Plant:
    """Represents a plant in the garden with basic, secure attributes"""
    plant_type = "regular"

    def __init__(self, name: int, height: int, age: int) -> None:
        """Initialize a Plant instance with
        name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        else:
            self.name = name
            self._height = height
            self._age = age

    def grow(self, growth: int = 1, time: int = 1) -> int:
        """Raises a Plant instance's height"""
        if growth <= 0:
            print("Growth can't be negative or zero [REJECTED]")
            return 0
        for _ in range(time):
            self._height += growth
        return growth * time

    def describe(self) -> None:
        """Prints a Plant instance's name and current height"""
        print(f"- {self.name}: {self._height}cm")


class FloweringPlant(Plant):
    """Represents a flowering plant in the garden with specific attributes"""
    plant_type = "flowering"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str = "unknown",
        blooming: bool = True,
    ) -> None:
        """Initialize a FloweringPlant instance with all Plant attributes
        as well as color and a booleans for blooming status"""
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming

    def describe(self) -> None:
        """Defines a blooming status and prints a FloweringPlant
        instance's name, current height, color and blooming status"""
        if self.blooming is True:
            status = "(blooming)"
        else:
            status = "(not blooming)"
        print(
            f"- {self.name}: {self._height}cm, {self.color} flowers {status}"
            )


class PrizeFlower(FloweringPlant):
    """Represents a prize flower in the garden with specific attributes"""
    plant_type = "prize"

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str = "unknown",
        blooming: bool = True,
        prize_points: int = 0
    ) -> None:
        """Initialize a PrizeFlower instance with all FloweringPlant attributes
        as well as prize points"""
        super().__init__(name, height, age, color, blooming)
        self.prize_points = prize_points

    def describe(self) -> None:
        """Defines a blooming status and prints a FloweringPlant
        instance's name, current height, color and blooming status"""
        if self.blooming is True:
            status = "(blooming)"
        else:
            status = "(not blooming)"
        print(f"- {self.name}: {self._height}cm, {self.color}", end=' ')
        print(f"flowers {status}, Prize points: {self.prize_points}")


class GardenManager:
    """Manages multiple garden for each owner"""
    _total_gardens_managed: int = 0

    class GardenStats:
        """Helps calculate, register and manage garden data"""
        def __init__(self) -> None:
            """Initializes the class GardenStats with
            total plants added and total growth"""
            self.plants_added = 0
            self.total_growth = 0

        def record_add(self) -> None:
            """Counts new plants added"""
            self.plants_added += 1

        def record_growth(self, growth: int) -> None:
            """Counts total growth of
            all the plants in a garden"""
            self.total_growth += growth

        def count_types(self, plant_list: list) -> None:
            """Counts types of plants in a garden"""
            regular = 0
            flowering = 0
            prize = 0
            for p in plant_list:
                if p.plant_type == "prize":
                    prize += 1
                elif p.plant_type == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

    class Garden:
        """Represents a garden with an owner and multiple plants"""
        def __init__(self, owner: str) -> None:
            """Initializes a garden with its owner name and an
            empty plant list, as well as initializes its stats"""
            self.owner = owner
            self.plant_list = []
            self.stats = GardenManager.GardenStats()

        def add_plant(self, plant: Plant) -> None:
            """Adds a plant to a garden"""
            self.plant_list.append(plant)
            self.stats.record_add()

        def help_all_grow(self, growth: int = 1, time: int = 1) -> None:
            """Runs grow() and GardeStats.record_growth() for each
            plant in a garden, and prints results"""
            print(f"{self.owner} is helping all plants grow...")
            total_growth = 0
            for p in self.plant_list:
                plant_growth = p.grow(growth, time)
                total_growth += plant_growth
                self.stats.record_growth(plant_growth)
                print(f"{p.name} grew {plant_growth}cm")

        def report(self) -> None:
            """Runs describe() for each plant and prints other
            stats such as total plants, growth and plant types"""
            print(f"\n=== {self.owner}'s Garden Report ===")
            print("\nPlants in garden:")
            for p in self.plant_list:
                p.describe()
            regular, flowering, prize = self.stats.count_types(self.plant_list)
            print(f"Plants added: {self.stats.plants_added},", end=' ')
            print(f"Total growth: {self.stats.total_growth}cm")
            print(f"Plant types: {regular} regular, {flowering}", end=' ')
            print(f"flowering, {prize} prize flowers")

        def score(self) -> None:
            """Calculates the garden's score based on prize points,
            total height & growth and the amount of plants it has"""
            total_plants = 0
            total_height = 0
            total_prize = 0
            for p in self.plant_list:
                total_plants += 1
                total_height += p._height
                if p.plant_type == "prize":
                    total_prize += p.prize_points
            return total_height + total_prize + (10 * total_plants)

    def __init__(self):
        """Initializes the Garden Manager with an empty garden list"""
        self.gardens = {}

    def add_garden(self, owner: str) -> None:
        """Adds a new garden to a Garden Manager if the owner
        doesn't already have one in it"""
        if owner not in self.gardens:
            self.gardens[owner] = GardenManager.Garden(owner)
            GardenManager._total_gardens_managed += 1

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """Adds a plant to a garden within the Garden Manager"""
        if owner not in self.gardens:
            self.add_garden(owner)
        self.gardens[owner].add_plant(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def get_garden(self, owner: str) -> None:
        """Returns the garden of an owner"""
        return self.gardens.get(owner)

    @staticmethod
    def validate_non_negative(value: int) -> None:
        """Returns False if value is negative"""
        return value >= 0

    @classmethod
    def total_gardens_managed(cls) -> None:
        """Returns the total amount of gardens from all managers"""
        return cls._total_gardens_managed

    @classmethod
    def create_garden_networks(cls, owners: tuple) -> None:
        """Creates and initializes one
        garden for each owner in a list"""
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    def garden_scores(self) -> None:
        """Runs score() for each existing garden and returns a dict"""
        scores = {}
        for owner, garden in self.gardens.items():
            scores[owner] = garden.score()
        return scores


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_networks(("Alice", "Bob"))

    oak = Plant("Oak Tree", 100, 1825)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", True, 10)

    manager.add_plant_to_garden("Alice", oak)
    manager.add_plant_to_garden("Alice", rose)
    manager.add_plant_to_garden("Alice", sunflower)

    bob_plant = Plant("Basil", 82, 20)
    manager.add_plant_to_garden("Bob", bob_plant)

    alice_garden = manager.get_garden("Alice")
    alice_garden.help_all_grow(1, 1)
    alice_garden.report()

    validation_result = GardenManager.validate_non_negative(1)
    print(f"Height validation test: {validation_result}")

    scores = manager.garden_scores()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")

    total = GardenManager.total_gardens_managed()
    print(f"Total gardens managed: {total}")
