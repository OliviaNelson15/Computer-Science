#Randomizer
from adafruit_circuitplayground import cp


while True:
    x, y, z = cp.acceleration
    shake_threshold = 15.0
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:

#Not done.