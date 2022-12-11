import usb_cdc as pico_serial


def configurations():
    pico_serial.enable(console=True, data=True)


configurations()