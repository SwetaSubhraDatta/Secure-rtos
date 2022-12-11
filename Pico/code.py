from lib.host import Host
from lib.device_info import DEVICENAME,DEVICEID

def activate_host():
    host=Host()
    print("Starting"+DEVICENAME +"ID:"+DEVICEID)
    while(True):
        json_dict=host.get_commands()
        if json_dict is not None:
            print("Status: Received commands")
        else:
            continue
        host.verify_commands(din=json_dict)
        host.send_report()

activate_host()
        




    