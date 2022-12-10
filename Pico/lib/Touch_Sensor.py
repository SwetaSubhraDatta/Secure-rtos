import digitalio
import analogio

class Touch_sensor:
    def __init__(self, pin):
        self.pin = pin
        self.touch = digitalio.DigitalInOut(pin)
        self.touch.direction = digitalio.Direction.INPUT
        self.touch.pull = digitalio.Pull.UP
        

    def is_pressed(self):
        return self.touch.value

    def __str__(self):
        return "Touch sensor on pin " + str(self.pin)


class LDR:
    def __init__(self, pin):
        self.pin = pin
        self.ldr = analogio.AnalogIn(pin)

    def __str__(self):
        return "LDR on pin " + str(self.pin)

    def value(self):
        return self.ldr.value

    def light(self):
        return self.ldr.value/ 100

