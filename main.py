import math

angle = 30
velocity = 10
gravity = -9.8

veloY = math.sin(
    math.radians(angle)
    )
veloY = veloY * 10
print(f'10 * sin{angle} = Vy')
print(str(veloY) + ' ')

Vf = veloY * -1
Vx = veloY
Vy = Vf - Vx
print(f'Vf = {Vf}')
print(f'Vx = {veloY}')
print(Vy)

deltaT = Vy / gravity
print(f'deltaT (time in seconds) = {deltaT}')


adj = velocity * math.cos(
    math.radians(angle)
    )
    
print(f'adj = {adj}')

distance = adj * deltaT

print(f'distance = {distance}m')
