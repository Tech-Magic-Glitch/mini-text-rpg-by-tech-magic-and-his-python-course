from characters import *

Name = input("Enter your name: ")
player = Player(Name)
player.show()








print(f"Welcome, {Name}! Welcome to only fight, a game where you can fight monsters and gain experience points to level up your character. Good luck on your journey! Type in 'quit' to exit the game at any time.")
print('Please select one of the following numbers to choose your rival:')
print('1. Goblin')
print('2. Orc')
print('3. Dragon')
print('4. Dragon Rider')
print('5. Dragon Lord')

while True:
 rival = input('Enter the number of your rival: ')
 if rival == '1':
  goblin = Goblin()
  [Goblin]
  player.fight(goblin)
 if rival == '2':
  orc = Orc()
  player.fight(orc)

 if rival == '3':
  Dragon = Dragon()
  player.fight(Dragon)
 if rival == '4':
  Dragon_Rider = Dragon_Rider()
  player.fight(Dragon_Rider)

 if rival == '5':
  Dragon_Lord = Dragon_Lord()
  player.fight(Dragon_Lord)
 if rival == quit:
  print('Thanks for playing! Goodbye!')
  break
