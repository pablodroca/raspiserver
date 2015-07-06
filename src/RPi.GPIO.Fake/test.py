import RPi.GPIO as gpio
from time import sleep

#gpio.debug = True


def showvalue(pins):
    for pin in pins:
        print("%s " % gpio.input(pin), end="")
    print()

gpio.setmode(gpio.BCM)
gpio.setup(22, gpio.OUT)
gpio.setup(23, gpio.OUT)
print("Alternating 2 pins")

for _ in range(4):
    gpio.output(22, gpio.HIGH)
    gpio.output(23, gpio.LOW)
    showvalue((22, 23))
    sleep(0.1)
    gpio.output(22, gpio.LOW)
    gpio.output(23, gpio.HIGH)
    showvalue((22, 23))
    sleep(0.1)
