from lib.rtos_routine import routine
from lib.host import Host

def activate_host():
    host=Host()
    while(True):
        json_dict=host.get_commands()
        if json_dict is not None:
            print("Status: Received commands")
        else:
            continue
        print(json_dict)
        




    