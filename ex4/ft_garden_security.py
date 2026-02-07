class SecurePlant:
    """Represents a plant in the garden with basic, secure attributes"""
    def __init__(self, name: str, height: int, age: int):
        """Initialize a SecurePlant with name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        else:
            self.name = name
            self._height = height
            self._age = age

    def get_info(self):
        """Prints information about a SecurePlant instance"""
        print(f"Current plant: {self.name}", end=" ")
        print(f"({self._height}cm, {self._age} days)")

    def get_height(self) -> int:
        """Getter Method to return height"""
        return self._height

    def set_height(self, new_height: int):
        """Setter Method to change height"""
        if new_height < 0:
            print("Operation REJECTED: height must be a non-negative value")
            print(f"{self.name}'s height can't be set to {new_height}cm")
        else:
            self._height = new_height
            print(f"{self.name}'s height updated: {new_height}cm [OK]")

    def get_age(self) -> int:
        """Getter Method to return age"""
        return self._age

    def set_age(self, new_age: int):
        """Setter Method to change age"""
        if new_age < 0:
            print("Operation REJECTED: age must be a non-negative value")
            print(f"{self.name}'s age can't be set to {new_age} days")
        else:
            self._age = new_age
            print(f"{self.name}'s age updated: {new_age} days [OK]")


if __name__ == "__main__":
    print("=== Garden Security System ===\n")
    print("== Rose ==")
    rose = SecurePlant("Rose", 15, 5)
    print(f"Plant created: {rose.name}\n")
    rose.get_info()
    rose.set_height(20)
    rose.set_age(6)
    rose.get_info()
    print("\n")
    print("== Cactus ==")
    cactus = SecurePlant("Cactus", 40, 10)
    print(f"Plant created: {cactus.name}\n")
    cactus.get_info()
    cactus.set_height(-5)
    cactus.set_height(-42)
    cactus.get_info()
    print("\n")
    print("== Sunflower ==")
    sunflower = SecurePlant("Sunflower", -5, 30)
    print("Plant not created\n")
