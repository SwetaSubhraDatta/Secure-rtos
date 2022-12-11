import serial
import json
import time

class Host_serial:
    def __init__(self, port="/dev/ttyACM1", baud=9600, timeout=5):
        self.serial = serial.Serial(port, baud, timeout=timeout)

    def receive(self) -> str:
        """
        This function helps to receive the data from the slave pico device
        """
        response = str(self.serial.readline(), "utf-8")
        return response

    def send(self, text: str) -> bool:
        """
        This function helps to send a data line to the slave pico device.
        Can be used for testing purposes.
        """
        line = text + "\n"
        self.serial.write(line.encode("ascii"))
        # the line should be echoed.
        # If it isn't, something is wrong.

    def send_comand(self, file: str = "Host/json/example.json"):
        """
        This function helps to send the commands in json format to the slave pico device
        """
        # load the json file
        with open(file) as json_f:
            json_file_ = json.load(json_f)
            stringify_json = json.dumps(json_file_)
            stringify_json = stringify_json + "\n"
            self.serial.write(stringify_json.encode("ascii"))

    def close(self):
        """
        This function helps to close the serial connection
        """
        self.serial.close()

        