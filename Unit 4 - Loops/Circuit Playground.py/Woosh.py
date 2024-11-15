from adafruit_circuitplayground import cp
import time

#Turn each pixel on / off INDIVIDUALLY, #13 total
#AKA repeatedely set them to desired color, then to black.
#Try to see what you can do about time. He said to
#Tell it to wait one second. (Or perhaps not, we already turned them off...)
#Now figure out how to turn them OFF individually
#Figure out how to do it in 7 lines
while True[0,1,2,3,4,5,6,7,8,9]:
    if cp.button_a:
         cp.pixels.fill((5, 3, 87))
         time.sleep((0,100))
         while cp.button_a:
            pass
    else:
        cp.pixels.fill((0,0,0))
    
#CURRENTLY UNFINISHED.