from lib.usb_serial import Serial
from lib.sensors import Touch_sensor
from lib.sensors import LDR
from lib.utils import pico_pinout as pin
from lib.device_info import DEVICENAME,DEVICEID


class Host:
    def __init__(self) -> None:
        self.usb = Serial()
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
    def verify_commands(self,din):
        """
        This function performs an mcu level verification of the host system
        """
        ##Veirifying the device names and the device id sent by the host system
        if  "DeviceName" in din:
            if(din["DeviceName"] == DEVICENAME):
                if("DeviceID" in din):
                    if (din["DeviceID"] == DEVICEID):
                        self.dout["DeviceName"]="pico" ##report generation
                        self.dout["DeviceID"]="001"
                        self.dout["DeviceVerified"]=True
                        self.dout["DeviceSensor"]={}
                    
            ##Verifying the device sensors
            if "sensor" in din["DeviceSensor"]:
                sensor_dict=din["DeviceSensor"]
                if sensor_dict["sensor"]=="touch": ##Touch sensor jobs
                    touch_pin=pin(int(sensor_dict["pins"][0]))
                    readings=sensor_dict["readings"]
                    self.dout["DeviceSensor"]["touch"]={}
                    self.touch_sensor_jobs(touch_pin=touch_pin,readings=readings)
                
    def send_report(self):
        """
        This function helps to send the report to the host system
        """
        print(self.dout)
        self.usb.write(self.dout)
        self.dout.clear()
    
    def touch_sensor_jobs(self,touch_pin,readings):
        """
        Touch sensor specific parsing and jobs for the touch sensor to
        be sent
        """
        reads=0
        try:
            self.touch=Touch_sensor(pin=touch_pin)
        except Exception as e:
            self.dout["DeviceSensor"]["touch"].clear()
            self.dout["Error"]=str(e)
            return
        self.dout["DeviceSensor"]["touch"]["verified"]=True
        self.dout["DeviceSensor"]["touch"]["values"]=[]
        while(reads<readings):
            self.dout["DeviceSensor"]["touch"]["values"].append(self.touch.is_pressed())
            reads+=1
        self.touch.deinit()
    
    def ldr_sensor_jobs(self):
        """
        ldr sensor
        """
        return
    
