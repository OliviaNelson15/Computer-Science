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
    #cp.pixels[0]=
    #cp.pixels[1]=
    #cp.pixels[2]=
    #cp.pixels[3]=
    #cp.pixels[4]=
    #cp.pixels[5]=
    #cp.pixels[6]=
    #cp.pixels[7]=
    #cp.pixels[8]=
    #cp.pixels[9]=
    #cp.pixels[10]=
    #cp.pixels[11]=
    #cp.pixels[12]=
    #cp.pixels[13]=


#If you have a single red light on your board, then it's working!
#...remember to save...

import time
from adafruit_circuitplayground import cp


while True:
    cp.pixels.fill((0,255,0))
    time.sleep((0,367))
    cp.pixels.fill((0,0,0))
    time.sleep((0,367))
    