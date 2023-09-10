# --------------------------------------------------------------------------------
# Module 7: Object-Oriented Programming (OOP)
# Section 1.2: Real-World Analogy of OOP - Python Examples
# --------------------------------------------------------------------------------

# -------------------------------------
# Example 1: Toy Car Class
# -------------------------------------
class ToyCar:
    def __init__(self, color, size, brand, doors):
        self.color = color
        self.size = size
        self.brand = brand
        self.doors = doors

    def move_forward(self):
        return "The car is moving forward!"

    def move_backward(self):
        return "The car is moving backward!"

    def honk(self):
        return "Honk! Honk!"

# Create an instance of ToyCar
car1 = ToyCar("Red", "Small", "Hot Wheels", 2)
print(car1.honk())

# -------------------------------------
# Example 2: Doll Class
# -------------------------------------
class Doll:
    def __init__(self, name, outfit, accessories):
        self.name = name
        self.outfit = outfit
        self.accessories = accessories

    def speak(self):
        return "Hello there!"

    def move_arms(self):
        return "Moving arms."

    def blink_eyes(self):
        return "Blinking eyes."

# Create an instance of Doll
doll1 = Doll("Anna", "Princess Dress", ["Crown"])
print(doll1.speak())

# -------------------------------------
# Example 3: Video Game Character Class
# -------------------------------------
class GameCharacter:
    def __init__(self, name, health, strength, inventory=[]):
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = inventory

    def attack(self, enemy):
        return f"{self.name} is attacking {enemy.name}!"

    def defend(self):
        return f"{self.name} is defending."

    def pick_up_loot(self, loot):
        self.inventory.append(loot)
        return f"{self.name} picked up {loot}."

    def drink_potion(self):
        self.health += 20
        return f"{self.name}'s health increased by 20."

    def level_up(self):
        self.strength += 10
        return f"{self.name}'s strength increased by 10."

# Create instances for GameCharacter
player = GameCharacter("Arthur", 100, 50)
enemy = GameCharacter("Goblin", 40, 20)
print(player.attack(enemy))

# Additional Classes for loot and enemies can be expanded upon based on game dynamics.

# --------------------------------------------------------------------------------
