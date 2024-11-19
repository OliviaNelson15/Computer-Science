from adafruit_circuitplayground import cp
#import time

#cp.pixels.brightness = 0.3

#while True:
        #cp.pixels.fill((0,255,0))
        #time.sleep(0.367)
        #cp.pixels.fill((0,0,0))
        #time.sleep(0.367)


#THERMOMETER

cp.pixels.brightness = 0.3

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32
    if temp_c < 78:
        cp.pixels[0] = ((0,0,1))
        cp.pixels[1] = ((0,0,1))
    elif temp_c > 79:
        cp.pixels[2] = ((0,0,1))

    if temp_c > 80:
        cp.pixels[3] = ((1,1,0))
    elif temp_c > 80:
        cp.pixels[4] = ((1,1,0))
    if temp_c > 82:
        cp.pixels[5] = ((1,1,0))
    cp.pixels[6] = ((1,1,0))
    cp.pixels[7] = ((1,0,0))
    cp.pixels[8] = ((1,0,0))
    cp.pixels[9] = ((1,0,0))

    #NOT DONE YET