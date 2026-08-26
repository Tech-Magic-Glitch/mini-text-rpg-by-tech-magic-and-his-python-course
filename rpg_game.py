from characters import *

name = input("Enter your name: ")
player = Player(name)
player.show()

goblin = Goblin()
orc = Orc()

# print(f"{goblin.name}: {goblin.hp}/{goblin.max_hp} HP {goblin.attack_power} ATK")
# print(f"{orc.name}: {orc.hp}/{orc.max_hp} HP {orc.attack_power} ATK")

player.fight(goblin)