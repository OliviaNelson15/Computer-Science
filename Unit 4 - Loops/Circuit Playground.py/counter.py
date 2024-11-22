from adafruit_circuitplayground import cp
#import time

#cp.pixels.brightness = 0.3

#while True:
        #cp.pixels.fill((0,255,0))
        #time.sleep(0.367)
        #cp.pixels.fill((0,0,0))
        #time.sleep(0.367)


#Counter

#He said to create a variable that counts the number of lights that
#Are on, and add 1 when the a buton is pressed. For button b,
#Subtract one each time it's pressed.

lol1 = cp.pixels((6, 54, 74))
lol2 = cp.pixels - 1

while True:
    if cp.button_a:
        lol1[0]
    
    


        #Currently unfinished
        #This is lowkey giving me a headache, Imma try something else for now