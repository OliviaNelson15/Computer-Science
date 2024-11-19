from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3

while True:
    if cp.switch:
        cp.pixels[0] = ((6, 99, 31))  #Green
        cp.pixels[1] = ((6, 99, 31))
        cp.pixels[2] = ((6, 99, 31))
        cp.pixels[3] = ((6, 99, 31))
        cp.pixels[4] = ((6, 99, 31))
        cp.pixels[5] = ((0, 0, 0))
        cp.pixels[6] = ((0, 0, 0))
        cp.pixels[7] = ((0, 0, 0))
        cp.pixels[8] = ((0, 0, 0))
        cp.pixels[9] = ((0, 0, 0))
    else:
        cp.pixels[0] = ((0, 0, 0))
        cp.pixels[1] = ((0, 0, 0))
        cp.pixels[2] = ((0, 0, 0))
        cp.pixels[3] = ((0, 0, 0))
        cp.pixels[4] = ((0, 0, 0))
        cp.pixels[5] = ((6, 99, 31))
        cp.pixels[6] = ((6, 99, 31))
        cp.pixels[7] = ((6, 99, 31))
        cp.pixels[8] = ((6, 99, 31))
        cp.pixels[9] = ((6, 99, 31))