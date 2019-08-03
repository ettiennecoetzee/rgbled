""" tested on ESP32, but will likely work on ESP8266

where variable "led": 0 is red, 2 is green, 3 is blue
default frequency is 1000Hz but can be manually set
mode will depend on if RGB led is common anode or common cathode
default mode is common anode, define change to common cathode

mode = 1: common anode
mode = anython else: common cathode
"""

from machine import Pin, PWM


class RGBLed:
    def __init__(self, red_pin, green_pin, blue_pin, freq=1000, mode=1):
        if mode == 1:
            off_duty = 1023
        else:
            off_duty = 0
        self.red_pin = PWM(Pin(red_pin), freq=freq, duty=off_duty)
        self.green_pin = PWM(Pin(green_pin), freq=freq, duty=off_duty)
        self.blue_pin = PWM(Pin(blue_pin), freq=freq, duty=off_duty)
        self.off_duty = off_duty
        self.on_duty = 1023 - off_duty

    def set_brightness(self,brightness):
        if brightness > 100:
            brightness = 100
        brightness = abs(self.off_duty - int(brightness * 10.23))
        self.green_pin.duty(brightness)
        self.red_pin.duty(brightness)
        self.blue_pin.duty(brightness)

    def set_led_brightness(self,led,brightness):
        if brightness > 100:
            brightness = 100
        brightness = abs(self.off_duty - int(brightness * 10.23))
        if led == 1:
            self.red_pin.duty(brightness)
        elif led == 2:
            self.green_pin.duty(brightness)
        elif led == 3:
            self.blue_pin.duty(brightness)

    def off(self,led=0):
        if led == 1:
            self.red_pin.duty(self.off_duty)
        elif led == 2:
            self.green_pin.duty(self.off_duty)
        elif led == 3:
            self.blue_pin.duty(self.off_duty)
        else:
            self.red_pin.duty(self.off_duty)
            self.green_pin.duty(self.off_duty)
            self.blue_pin.duty(self.off_duty)

    def on(self,led=0):
        if led == 1:
            self.red_pin.duty(self.on_duty)
        elif led == 2:
            self.green_pin.duty(self.on_duty)
        elif led == 3:
            self.blue_pin.duty(self.on_duty)
        else:
            self.red_pin.duty(self.on_duty)
            self.green_pin.duty(self.on_duty)
            self.blue_pin.duty(self.on_duty)

    def colour_8bit(self,red,green,blue):
        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255
        self.red_pin.duty(abs(self.off_duty - abs(red) * 4))
        self.green_pin.duty(abs(self.off_duty - abs(green) * 4))
        self.blue_pin.duty(abs(self.off_duty - abs(blue) * 4))

    def colour_roll_up(self,time_loop_seconds):
        import utime as time
        sleep_time = (time_loop_seconds/(256*7))
        red = 0
        blue = 0
        green = 0
        while red < 255:
            red += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while green < 255:
            green += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red > 0:
            red -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while blue < 255:
            blue += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while green > 0:
            green -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red < 255:
            red += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while green < 255:
            green += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)

    def colour_roll_down(self,time_loop_seconds):
        import utime as time
        sleep_time = (time_loop_seconds/(256*7))
        red = 255
        blue = 255
        green = 255
        while green > 0:
            green -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red > 0:
            red -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red > 0:
            red -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while green < 255:
            green += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while blue > 0:
            blue -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red < 255:
            red += 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while green > 0:
            green -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)
        while red > 0:
            red -= 1
            self.colour_8bit(red, green, blue)
            time.sleep(sleep_time)