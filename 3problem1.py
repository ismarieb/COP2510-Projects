# Driver: Ismarie Birriel
# Navigator: Lam Nguyen
# Program prompts user for x,y coordinates, direction and distance
# to calculate final position using x,y coordinates

x = int(input('Enter the x-coordinate: '))
y = int(input('Enter the y-coordinate: '))
direction = input('Enter the direction (up, down, left, or right): ')
distance = int(input('Enter the distance to move: '))

if direction not in ['up', 'down', 'left', 'right']:
    print('Invalid direction')
    print(f'Original location is ({x},{y}).')

if direction == 'up':
    y = y + distance

if direction == 'down':
    y = y - distance

if direction == 'left':
    x = x - distance

if direction == 'right':
    x = x + distance

print(f'The final destination is ({x},{y}).')
