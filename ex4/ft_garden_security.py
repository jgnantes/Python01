class SecurePlant:
    """Represents a plant in the garden with basic, secure attributes"""
    def __init__(self, name, height, age):
        """Initialize a SecurePlant with name, height (cm) and age in days"""
        if height < 0 or age < 0:
            raise ValueError("Both height and age must be non-negative values")
        self.name = name
        self._height = height
        self._age = age

    def get_info(self):
        """Prints information about a SecurePlant instance"""
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def get_height(self):
        """Getter Method to return height"""
        return self._height

    def set_height(self, new_height):
        """Setter Method to change height"""
        if new_height < 0:
            raise ValueError("Height must be a non-negative value")
        self._height = new_height

    def get_age(self):
        """Getter Method to return age"""
        return self._age

    def set_age(self, new_age):
        """Setter Method to change age"""
        if new_age < 0:
            raise ValueError("Age must be a non-negative value")
        self._age = new_age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 5)
    rose.get_info()
    rose.set_height(20)
    rose.set_age(6)
    rose.get_info()
    cactus = SecurePlant("Cactus", 5, 5)
    cactus.get_info()
    cactus.set_height(-5)
