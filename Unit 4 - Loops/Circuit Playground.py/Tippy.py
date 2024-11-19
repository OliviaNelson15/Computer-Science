from adafruit_circuitplayground import cp

#Tippy

cp.pixels.brightness = 0.3

while True:
    x, y, z = cp.acceleration
    if x < -5:
        cp.pixels[1] = ((6, 99, 31))  #Green
        cp.pixels[2] = ((6, 99, 31))
        cp.pixels[3] = ((6, 99, 31))
        cp.pixels[0] = ((0, 0, 0))
        cp.pixels[4] = ((0, 0, 0))
        cp.pixels[5] = ((0, 0, 0))
        cp.pixels[6] = ((0, 0, 0))
        cp.pixels[7] = ((0, 0, 0))
        cp.pixels[8] = ((0, 0, 0))
        cp.pixels[9] = ((0, 0, 0))
    elif x > 5:
        cp.pixels[6] = ((99, 6, 6))   #Red
        cp.pixels[7] = ((99, 6, 6))
        cp.pixels[8] = ((99, 6, 6))
        cp.pixels[0] = (0,0,0)
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,0)
        cp.pixels[4] = (0,0,0)
        cp.pixels[5] = (0,0,0)
        cp.pixels[9] = (0,0,0)
