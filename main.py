from Host.serial_interface import Host_serial as Host


def select_json(json_file):
    return json_file

def verify_json(json_file):
    return json_file

if __name__ == "__main__":
        host = Host("/dev/ttyS1")
        host.send_comand()
        host.close()
  