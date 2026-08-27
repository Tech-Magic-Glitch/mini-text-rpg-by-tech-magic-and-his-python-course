import random, time

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack

    def is_alive(self):
        return self.hp > 0

    def show(self):
        print(f"{self.name}: {self.hp}/{self.max_hp} HP")

    def attack(self, target):
        damage = random.randint(1, self.attack_power)
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
        print(f"{self.name} deals {damage} damage to {target.name}")
        target.show()
        time.sleep(0.8)
        return damage

class Hero(Character):
    def __init__(self, name, level = 1):
        super().__init__(name, hp = 100, attack = 10)
        self.level = level

    def fight(self, enemy):
        while self.is_alive() and enemy.is_alive():
            self.attack(enemy)
            if enemy.is_alive():
                enemy.attack(self)

class Player(Hero):
    def __init__(self, name):
        super().__init__(name, level = 1)
        self.xp = 0
        self.inventory = []

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 10:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0 # XP reset
        self.max_hp += 5
        self.attack_power += 2
        self.hp = self.max_hp # heilen bei lvl up
        print(f"{self.name} advanced to level {self.level}")

    def fight(self, enemy):
        super().fight(enemy)
        if self.is_alive:
            self.gain_xp(enemy.xp_reward)
            print(f"{self.name} gained {enemy.xp_reward} XP")
        else:
            print(f"{self.name} WAS DEFEATED IN BATTLE !!!! 😭😭😭😭😭")

class Monster(Character):
    def __init__(self, name, hp, attack, xp_reward):
        super().__init__(name, hp, attack)
        self.xp_reward = xp_reward

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", hp = 15, attack = 10, xp_reward = 7)

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", hp = 30, attack = 7, xp_reward = 11)

class Sceleton(Monster):
    def __init__(self):
        super().__init__('Sceleton', hp = 20, attack = 5, xp_reward = 9)

class Dragon(Monster):
    def __init__(self, name, hp, attack, xp_reward):
        super().__init__('Dragon', hp = 25, attack = 15, xp_reward = 15)

class Dragon_Rider(Monster):
    def __init__(self, name, hp, attack, xp_reward):
        super().__init__('Bad Dragon Rider', hp = 35, xp_reward = 25)

class Dragon_Lord(Monster):
    def __init__(self, name, hp, attack, xp_reward):
        super().__init__('Rainer der verwinkelte Drachenlord', hp = 50, xp_reward = 30)