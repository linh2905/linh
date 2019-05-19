import random

map_height = int(input('Enter map height: '))
map_width = int(input('Enter map width: '))

player = {
    'x': random.randint(0,map_width-1),
    'y': random.randint(0,map_height-1),
    'key': 0,
}
while True:
    key_1 = {
    'x' : random.randint(0,map_width-1),
    'y' : random.randint(0,map_height-1),
    }
    if key_1['x'] != player['x'] and key_1['y'] != player['y']:
        break

while True:
    key_2 = {
    'x' : random.randint(0,map_width-1),
    'y' : random.randint(0,map_height-1),
    }
    if key_2['x'] != player['x'] and key_2['y'] != player['y'] and key_2 != key_1:
        break

while True:
    exit = {
    'x' : random.randint(0,map_width-1),
    'y' : random.randint(0,map_height-1),
}
    if exit['x'] != player['x'] and exit['y'] != player['y'] and exit != key_1:
        break

while True:
    wall = {
    'x' : random.randint(0,map_width-1),
    'y' : random.randint(0,map_height-1),
}
    if wall['x'] != player['x'] and wall['y'] != player['y'] and wall != key_1 and wall != exit and wall != key_2:
        break

while True: 
    wall_2 = {
    'x' : random.randint(0,map_width-1),
    'y' : random.randint(0,map_height-1),
}
    if wall_2 != wall and wall_2['x'] != player['x'] and wall_2['y'] != player['y'] and wall_2 != key_1 and wall_2 != exit and wall_2 != key_2:
        break

while True:

    for y in range(map_height):
        for x in range(map_width):
            if x == player['x'] and y == player['y']:
                print("P",end=" ")
            elif x == key_1['x'] and y == key_1['y']:
                print("K", end = ' ')
            elif x == key_2['x'] and y == key_2['y']:
                print("K", end = ' ')
            elif x == exit['x'] and y == exit['y']:
                print('E', end=' ')
            elif x == wall['x'] and y == wall['y']:
                print('W', end =' ')
            elif x == wall_2['x'] and y == wall_2['y']:
                print('W', end =' ')
            else:
                print('_', end=" ")
        print(' ')
    move = input('Your move: ').upper()

    fake = {
        'x': player['x'],
        'y': player['y'],
    }
    
    if move == "W":
        fake['y'] -=1
        if fake == wall:
            fake['y'] +=1
            print('Cannot move')
    elif move == "A":
        fake['x'] -=1
        if fake == wall:
            fake['x'] +=1
            print('Cannot move')
    elif move == "S":
        fake['y'] +=1
        if fake == wall:
            fake['y'] -=1
            print('Cannot move')
    elif move == "D":
        fake['x'] +=1
        if fake == wall:
            fake['x'] -=1
            print('Cannot move')

    if fake['x'] in range(map_width) and fake['y'] in range(map_height):
        player['x'] = fake['x']
        player['y'] = fake['y']



    if player['x'] == key_1['x'] and player['y'] == key_1['y']:
        player['key'] +=1
        key_1 = {
            'x': -1,
            'y': -1,
        }

    if player['x'] == key_2['x'] and player['y'] == key_2['y']:
        player['key'] +=1
        key_2 = {
            'x': -1,
            'y': -1,
        }

    if player['x'] == exit['x'] and player['y'] == exit['y']:
        # player['key'] -= 1
        
        if player['key'] != 2:
            print('You must find the key first!')
        else:
            exit = { 
            'x' : -1,
            'y' : -1,
        }
            print('Congratulations! You have escaped!')
            break
        
        


        
        
    

        

    

    




        
    


        




