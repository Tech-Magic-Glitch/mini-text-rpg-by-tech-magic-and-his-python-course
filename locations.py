import random, time, os
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

    def enter(self, player):
        self.player = player

        # add inventory to actions
        self.actions["inventory"] = self.player.use_item

        print(f"Location: {self.description}")

        # enter loop
        while True:
            print("Options: ")
            # for loop to print all options
            for option in self.actions:
                print(f"- {option}")

            # treffe wahl bis richtig gewählt
            choice = input("Choose an option: ")
            while choice not in self.actions:
                print("Invalid choice.")
                choice = input("Choose an option: ")

            # choice ausführen
            if self.actions[choice]():
                break

    def leave(self):
        return True

    def rest(self):
        print("You rest and regain your strength")
        self.player.hp = self.player.max_hp

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