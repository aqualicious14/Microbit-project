from microbit import *
import radio
#stall has 2 microbits to handle the 2 tasks of assigning orders and finishing orders
#stall microbit two (completed orders)
#only works in version 2
radio.on()
radio.config(channel = 2)
completed_order = 0
while True:
    a = button_a.was_pressed()
    b = button_b.was_pressed()
    c = pin_logo.is_touched()
    if a:
        completed_order += 1
        radio.send(str(completed_order))
        display.scroll(str(completed_order))
        #go between completed order numbers (+)
    if b:
        completed_order -= 1
        if completed_order < 0:
            orderno = 0
        display.scroll(completed_order)
        #go between completed order numbers (-)
    if c:
        radio.send(str(completed_order))
        #to alert customer of their completed order

#the customer microbits are switched off until they need to be given to the customer
#to reset numbers every day, run code again the next day to restart everyday
