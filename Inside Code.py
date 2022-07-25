#adventure game
import time

print('Welcome to Santa Cruz Mountain Adventure Game!')
print('**********************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike alone in the mountains.')
print('You can pick one item to take with you - ')
print('map(m), flashlight(f), chocolate(c), rope(r), or sticks(s): ')
item = input('What do you choose?: ')
print('You hear a humming sound.')
choice1 = input('Do you follow the sound? Enter y or n: ')
while not (choice1 == 'y' or choice1 == 'n'):
  choice1 = input('That is an invalid response. Enter y or n: ')
if choice1 == 'y':
  print('You keep moving closer to the sound.')
  print('The sound suddenly stops.')
  time.sleep(3)
  print('You are now LOST! ... ')
  time.sleep(3)
  print('You try to call on your phone, but there is no signal!')
direction = input('Which direction do you go? north, south, east, or west: ')
if direction == 'north':
  print('You reached an abandoned cabin.')
  if item == 'm':
    print('You use the map and find your way home.')
    print('CONGRATULATIONS! You won the game. ')
  else:
    print('If you had a map, you could find your way home from here.')
    print('---You are still lost. You lost the game.---')
elif direction == 'south':
  print('You reach a river with a broken bridge.')
  if item == 'r' or item == 's':
    print('You chose the item that can help fix the bridge.')
    print('You fix that bridge and find that it leads to an old hiking trail')
    print('You follow the trail back to the city')
    print('CONGRATULATIONS! You won the game.')
    else:
      print('If you had some rope or sticks, you could fix the bridge.')
      print('---You are still lost, You lost the game.---')
 elif direction == 'west':
  print('You are walking and you trip over a fallen log.')
  print('You have hurt your foot. You sit down to wait for help.')
  print('This could be along time. You are still lost.')
  print('---You lost the game.---')
  else:
    print('You reach the side of the highway. It is dark.')
    if item == 'f':
      print('You can use the flashlight to signal.')
      print('A car stops and gives you a ride home.')
      print('CONGRATULATIONS! You won the game.')
    else:
      print('If you had a flashlight you could signal for help.')
      print('---You are stll lost. You lost the game.---')
else:
  print('Good idea. You are not taking risks. ')
  print('You start walking back to the starting point.')
  print('You realize you are LOST! ')
  print('The sound is behind you and getting louder. You panic! ')
  action = input('Do you want to start running (r), or stop to make a call (c)?: ')
  while action == 'c':
    print('The call does not go through')
    action = input('D you want to start running (r), or try calling again (c)?: ')
  print('You are running fast. The sound gets really loud')
  print('A woman on an electric scooter comes up behind you.')
  anwser = input('she say, "Name my favorite computer programming language.": ')
  if answer.lower() == 'python':
    print('She says,"Yes, Python is my favorite programming language."')
    print('"If you have some chocolate I can help you."')
    if item == 'c':
      print('Luckily you chose correctly!')
      print('You give her the chocolate.')
      print('She helps you get home.')
      print('CONGRATULATIONS! You won the game.')
    else:
      print('You should have chosen that chocolate.')
      print('She rides away, leaving you alone and lost.')
      print('---You lost the game.---')
  else:
    print('She did not like your answer.')
    print('She rides away, leaving you lost!')
    print('You lost the game.')
