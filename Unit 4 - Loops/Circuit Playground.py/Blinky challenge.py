#Drawer # 7

#Imports tools needed to interact with the board
#from adafruit_circuitplayground import cp
#Everything you write will go inside the "While true" loop.
#when the program finishes it enters a waitning state it flashes all green then off
#A pixel is made of 3 LEDS
#LEDS are manufactued to display one color
#They change brightness based on how much power the recive
#THe 3 values you set a pixel to are red, green, and blue values
#while True:    #13 total
    #cp.pixels[0]=(23, 128, 0)
    #cp.pixels[1]=(23, 128, 0)
    #cp.pixels[2]=(23, 128, 0)
    #cp.pixels[3]=(23, 128, 0)
    #cp.pixels[4]=(23, 128, 0)
    #cp.pixels[5]=(23, 128, 0)
    #cp.pixels[6]=(23, 128, 0)
    #cp.pixels[7]=(23, 128, 0)
    #cp.pixels[8]=(23, 128, 0)
    #cp.pixels[9]=(23, 128, 0)
    #cp.pixels[10]=(23, 128, 0)
    #cp.pixels[11]=(23, 128, 0)
    #cp.pixels[12]=(23, 128, 0)
    #cp.pixels[13]=(23, 128, 0)


#If you have a single red light on your board, then it's working!
#...remember to save...

from adafruit_circuitplayground import cp

#Blinky
def blink():
    while True:
        cp.pixels.fil((23, 128, 0))
    time.color((23,128,0))
    import time

    print(1)

    time.sleep(367)

    print(2)

blink()
#Update: currently blinking red at the wrong speed...
#Woosh

