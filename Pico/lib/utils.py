import board
import busio

def pico_pinout(pins: int):
    """
    This function converts the json_pin to pico_pin
    """
    assert 0 <= pins <= 28, "Pins must be between 1 and 28"
    if pins == 0:
        return board.GP0
    elif pins == 1:
        return board.GP1
    elif pins == 2:
        return board.GP2
    elif pins == 3:
        return board.GP3
    elif pins == 4:
        return board.GP4
    elif pins == 5:
        return board.GP5
    elif pins == 6:
        return board.GP6
    elif pins == 7:
        return board.GP7
    elif pins == 8:
        return board.GP8
    elif pins == 9:
        return board.GP9
    elif pins == 10:
        return board.GP10
    elif pins == 11:
        return board.GP11
    elif pins == 12:
        return board.GP12
    elif pins == 13:
        return board.GP13
    elif pins == 14:
        return board.GP14
    elif pins == 15:
        return board.GP15
    elif pins == 16:
        return board.GP16
    elif pins == 17:
        return board.GP17
    elif pins == 18:
        return board.GP18
    elif pins == 19:
        return board.GP19
    elif pins == 20:
        return board.GP20
    elif pins == 21:
        return board.GP21
    elif pins == 22:
        return board.GP22
    elif pins == 23:
        return board.GP23
    elif pins == 24:
        return board.GP24
    elif pins == 25:
        return board.GP25
    elif pins == 26:
        return board.GP26
    elif pins == 27:
        return board.GP27
    else:
        return board.GP28