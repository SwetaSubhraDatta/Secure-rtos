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

def parse_actual_values(din):
    values=[]
    json_file=json.loads(din)
    for c,i in enumerate(json_file["Task1"]["values"]):
        if not c&1:
            values.append(i)
    print(values)
    return values

if __name__ == "__main__":
        host = Host(port="/dev/cu.usbmodem1103")
        json_verified=verify_json(json_file="Host/json/tasks.json")
        while (json_verified):
            host.send_comand(file ="Host/json/tasks.json")
            print("tx:sent command to pico")
            print("Please wait for status responnse")
            time.sleep(2)
            din=host.receive()
            print("rx:"+din)
            parse_actual_values(din)
            break
        host.close()
  