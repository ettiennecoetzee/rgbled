from rgbled import RGBLed
import utime as time

rgb = RGBLed(18,19,21) # red, green and blue pins of LED to GPIO of ESP (remember to add current limiting resistor)


if __name__ == '__main__':
    rgb.on()
    time.sleep(2)
    rgb.off()
    time.sleep(2)
    rgb.set_brightness(50) # brightness is percentage
    time.sleep(2)
    rgb.set_brightness(100)
    time.sleep(2)
    rgb.off()
    rgb.on(1)
    time.sleep(1)
    rgb.on(2)
    rgb.off(1)
    time.sleep(1)
    rgb.on(3)
    rgb.off(2)
    time.sleep(1)

    #colour roll through colour spectrum (8 bit) every 30 seconds
    
    while True:
        rgb.colour_roll_up(15)
        rgb.colour_roll_down(15)

