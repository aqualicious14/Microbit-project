from microbit import *
import radio
import music
#customer
radio.on()
tune = ["c4:4"]
flash = Image("99999:99999:99999:99999:99999")
radio.config(channel = 1)
while True:
    orderno = radio.receive()
    break
radio.config(channel = 2)
flag = True
while flag:
    completed_order = radio.receive()
    if completed_order == orderno:
        for i in range(10):
            music.play(tune)
            display.show(flash)
            sleep(100)
            display.clear()
        flag = False
    