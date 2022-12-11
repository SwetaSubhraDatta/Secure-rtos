import digitalio
import analogio

class Touch_sensor:
    __instance = None
    def __new__(cls, pin):
        """
        Singleton class
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, pin):
        self.pin = pin
        self.touch = digitalio.DigitalInOut(pin)
        self.touch.direction = digitalio.Direction.INPUT
        self.touch.pull = digitalio.Pull.UP
        

    def is_pressed(self):
        return self.touch.value

    def __str__(self):
        return "Touch sensor on pin " + str(self.pin)

    def deinit(self):
        self.touch.deinit()

class LDR:
    __instance = None
    def __new__(cls, pin):
        """
        Singleton class
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, pin):
        self.pin = pin
        self.ldr = analogio.AnalogIn(pin)

    def __str__(self):
        return "LDR on pin " + str(self.pin)

    def value(self):
        return self.ldr.value

    def light(self):
        return self.ldr.value/ 100

    def deinit(self):
        self.ldr.deinit()

