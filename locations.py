from characters import *
from items import Weapon, Potion
from  os import *
from  random import *
from  time import *

class Location:
    def __init__(self, name, description, monsters, loot_table):
        self.name = name
        self.description = description
        self.monsters = monsters
        self.loot_table = loot_table

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