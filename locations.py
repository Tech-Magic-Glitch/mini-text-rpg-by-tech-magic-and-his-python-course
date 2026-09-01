mport random, time, os
from characters import *
from items import Weapon, Potion

class Location:
    def __init__(self, name, description, characters, items):
        self.name = name
        self.description = description
        self.characters = characters
        self.items = items 
        self.actions = {
            "explore": self.explore,
            "rest": self.rest,
            "leave": self.leave
        }

    def enter():
        pass

    def leave():
        pass

    def rest():
        pass

    def explore():
        pass
    

forest = Location(
    "Forest",
    "A dense forest full of goblins",
    [Goblin, Goblin, Orc],
    [Potion(), Weapon("Spear", 3), Weapon("Slingshot", 1)]
)

cave = Location(
    "Cave",
    "A dark cave. You can smell orcs.",
    [Orc, Orc, Goblin],
    [Potion(), Weapon("Pickaxe", 5), Weapon("Club", 2)]
)

village = Location(
    "Village",
    "A peaceful village. You can rest here.",
    [],
    [Potion(), Potion()]
)