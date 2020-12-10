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
print(f'{velocity} * sin{angle} = Vy')
print(str(veloY) + ' ')

Vf = veloY * -1
Vx = veloY
Vy = Vf - Vx
print(f'Vf = {Vf}')
print(f'Vx = {veloY}')
print(Vy)

deltaT = Vy / gravity
print(f'deltaT = {Vy} / {gravity}')
print(f'deltaT (time in seconds) = {deltaT}')


adj = velocity * math.cos(
    math.radians(angle)
    )
    
print(f'adj = {adj}')

distance = adj * deltaT

print(f'distance = {distance}m')
