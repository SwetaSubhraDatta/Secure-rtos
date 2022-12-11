"""
This module in the library is pico_Communication Module
"""
import json
import sys

import usb_cdc


class Serial:
    """
    This  singleton class helps in interfacing the pico as a serial device
    and can only have one instance .NO more than one instance can be created
    without deleting the first instance
    """

    __instance = None

    def __new__(cls, *args):
        """
        This function helps to create a singleton class
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self) -> None:
        if usb_cdc.data is None:
            print(
                "Please check configuration in boot.py or checkout documentation: pico cannot find any data port"
            )
            sys.exit(1)
        self.serial_lock = False
        self.serial = usb_cdc.data

    def read(self):
        """
        This function helps to read the commands from host system
        """
        commands = None
        self.serial.reset_output_buffer()
        if self.serial.in_waiting != 0:
            commands = self.serial.readline().decode("utf-8")
            commands = json.loads(commands)
        return commands

    def close(self):
        """
        Closes the serial communication
        """
        self.serial.flush()
        self.serial = None
        print("Pico serial bus is closed")

    def lock_is_opened(self):
        """
        Get lock status
        """
        if not self.serial_lock:
            return True
        return False

    def lock(self):
        """
        locks the port and will not release it unless someone releases lock
        """
        if not self.serial_lock:
            self.serial_lock = True
        print("Cannot acquire lock,release the lock first")
        return self.serial_lock

    def release_lock(self):
        """
        When finished please release the lock so that you can call other objects
        or someone can use the sensor
        """
        if not self.serial_lock:
            self.serial_lock = False
            return self.serial_lock
        print("Serial is already unlocked")
        return self.serial_lock

    def write(self, msg: dict):
        """
        Writes a message as a serial communication
        """
        self.serial.reset_input_buffer()
        if "Spectral" in msg:
            data = json.dumps(msg["Spectral"])
        data = bytes("spectral:" + data + ":::", "utf-8")
        self.serial.write(data)
        self.serial.flush()

        if "Relay" in msg:
            data = json.dumps(msg["Relay"])
        data = bytes("Relay:" + data, "utf-8")
        self.serial.write(data)
        self.serial.flush()