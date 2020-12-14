import math # for sin, cos, and other math functions

# collect information from user
angle = float(input('Angle: '))
velocity = float(input('Velocity: '))
gravity = input('Gravity (leave blank for Earth\'s): ')

# handle if user wants earths gravity by inputing nothing
if gravity.strip() == '':
    gravity = -9.8
else:
    gravity = float(gravity)

# calculate veloY(not an official term)
# velocity * sin(angle)

# calculate sin(angle)
# convert angle to radians because python uses radians instead of degrees
veloY = math.sin( math.radians(angle) )
veloY = veloY * velocity
print(f'{velocity} * sin{angle} = Vy >')
print(' > ' + str(veloY))

# calculate Vx(the object rising) and (Vy the object falling)
Vf = veloY * -1
Vx = veloY
Vy = Vf - Vx # this number is important later for calculating deltaT
print(f'\nVf = {Vf}')
print(f'Vx = {veloY}')
print(f'Vy = {Vy} \n')

# calculate deltaT or the time spent in the air
deltaT = Vy / gravity
print(f'deltaT = {Vy} / {gravity}')
print('\033[95m' + f'deltaT (time in seconds) = {deltaT}s' + '\033[0m')  # bold output

# Calculate adj which is used for distance
adj = velocity * math.cos( math.radians(angle) ) # again convert to radians bc python uses them
print(f'\nadj = {velocity} * cos{angle} >')
print(f' > adj = {adj}')

distance = adj * deltaT  # finally calculate distance

print('\033[95m' + f'distance = {distance}m' + '\033[0m')  # bold output
