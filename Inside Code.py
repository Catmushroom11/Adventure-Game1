#adventure game

print('Welcome to Santa Cruz Mountain Adventure Game!')
print('**********************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike alone in the mountains.')
print('You can pick one item to take with you - ')
print('map(m), flashlight(f), chocolate(c), rope(r), or sticks(s): ')
item = input('What do you choose?: ')
print('You hear a humming sound.')
choice1 = input('Do you follow the sound? Enter y or n: ')
if choice1 == 'y':
  print('You keep moving closer to the sound.')
  print('The sound suddenly stops.')
  print('You are now LOST! ... ')
  print('You try to call on your phone, but there is no signal!')
  
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
