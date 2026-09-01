class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

    def use(self, player):
        print("You can't use this item!")
        return False # Item verschwindet NICHT nach use

class Potion(Item):
    def __init__(self):
        super().__init__("Healing Potion")

    def use(self, player):
        heal = 10 # amount to heal the player
        player.hp = min(player.max_hp, player.hp + heal)
        print(f"{player.name} heals for {heal} HP")
        return True # item verschwindet nach use

class Weapon(Item):
    def __init__(self, name, bonus):
        super().__init__(name)
        self.bonus = bonus

    def use(self, player):
        player.attack_power += self.bonus 
        print(f"{player.name} increased attack power by {self.bonus} ATK")
        return True # item verschwindet nach use