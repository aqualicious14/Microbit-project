from microbit import *
import radio
#stall has 2 microbits to handle the 2 tasks of assigning orders and finishing orders
#stall microbit one (assigning orders)
#only works in version 2
radio.on()
radio.config(channel = 1)
orderno = 0
while True:
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    c = pin_logo.is_touched()
    if a:
        orderno = orderno + 1
        radio.send(str(orderno))
        display.scroll(str(orderno))
        #go between order numbers (+)
    if b:
        orderno -= 1
        if orderno < 0:
            orderno = 0
        display.scroll(orderno)
        #go between order numbers (-)
    if c:
        radio.send(str(orderno))
        #to give customer microbit order number

#the customer microbits are switched off until they need to be given to the customer
#to reset numbers every day, run code again the next day to restart everyday
    
