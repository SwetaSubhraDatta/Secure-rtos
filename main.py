import time
import json
from Host.serial_interface import Host_serial as Host
from Verification_Layer.pydantic_validation import json_verify

def select_json(json_file):
    return json_file

def verify_json(json_file):
    with open (json_file) as json_f:
        json_load = json.load(json_f)
        json_file_verified = json_verify(json_load)
        return json_file_verified
if __name__ == "__main__":
        host = Host(port="/dev/cu.usbmodem1103")
        json_verified=verify_json(json_file="Host/json/example.json")
        while (json_verified):
            host.send_comand(file ="Host/json/example.json")
            print("tx:sent command to pico")
            print("Please wait for status responnse")
            time.sleep(2)
            print("rx:"+host.receive())
            break
        host.close()
  