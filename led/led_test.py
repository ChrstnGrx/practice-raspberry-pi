from gpiozero import LED
from time import sleep

light = LED(17)
i = 0

while True:
    light.on()
    sleep(1)
    light.off()
    sleep(1)
    i += 1
    print("Round " + str(i))
