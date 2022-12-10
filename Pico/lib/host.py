from lib.usb_serial import Serial
from lib.sensors import Touch_sensor
from lib.sensors import LDR


class Host:
    def __init__(self) -> None:
        self.serial = Serial()
        self.serial_lock = False #Not locking and unlocking the serial bus in this version,maybe in the future
        self.touch=None
        self.ldr=None
        self.dout={}

    
    def get_commands(self):
        """
        This function helps to get the commands from the host system
        """
        commands = self.usb.read()
        return commands
    def verify_commands(self):
        """
        This function performs an mcu level verification of the host system
        """
        
        
    def send_report(self):
        """
        This function helps to send the report to the host system
        """
        self.usb.write(self.dout)
    
    def touch_sensor_jobs(self):
        """
        Touch sensor specific parsing and jobs for the touch sensor to
        be sent
        """
        return
    
    def ldr_sensor_jobs(self):
        """
        ldr sensor
        """
        return
    
