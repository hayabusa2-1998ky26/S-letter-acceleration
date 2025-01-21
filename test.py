# import
import math

# parameters
min_speed = 20
max_speed = 100
accelerater = 10

speed = min_speed
speeds = []

# accel
for i in range(int(360 / accelerater)):
    acceleration = (1 - math.cos(math.radians(i * accelerater))) * (max_speed - min_speed) / (360 / accelerater)
    speed += acceleration
    speeds.append(speed)

# copy accel
speeds2 = speeds.copy()

# max speed
speeds += list(int(100 - (360 / accelerater * 2)) * [max_speed])

# decel
speeds += list(reversed(speeds2))

# screen
for i in speeds:
    print(int(i) * "-")
