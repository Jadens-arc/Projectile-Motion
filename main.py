import math

angle = int(input('Angle: '))
velocity = int(input('Velocity: '))
gravity = input('Gravity (leave blank for Earth\'s): ')
if gravity.strip() == '':
    gravity = -9.8
else:
    gravity = int(gravity)

veloY = math.sin(
    math.radians(angle)
    )
veloY = veloY * velocity
print(f'{velocity} * sin{angle} = Vy >')
print(' > ' + str(veloY))

Vf = veloY * -1
Vx = veloY
Vy = Vf - Vx
print(f'\nVf = {Vf}')
print(f'Vx = {veloY}')
print(f'Vy = {Vy} \n')

deltaT = Vy / gravity
print(f'deltaT = {Vy} / {gravity}')
print('\033[95m' + f'deltaT (time in seconds) = {deltaT}s' + '\033[0m')


adj = velocity * math.cos(
    math.radians(angle)
    )
print(f'\nadj = {velocity} * cos{angle} >')
print(f' > adj = {adj}')

distance = adj * deltaT

print('\033[95m' + f'distance = {distance}m' + '\033[0m')
