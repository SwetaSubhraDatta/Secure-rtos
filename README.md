# ece_591 
## Author Vishrut and Sweta 
## RP-2040-devices
This repo hosts all the sensors that will be interfaced with the rp2040 chip on pi pico. 

## Getting started
Hold the bootsel button and plug in the pi pico.
from the /uf2 files copy the adafruit-circuitpython-raspberry_pi_pico-en_US-(version)-alpha.1.uf2
and drag the uf2 file to pico  
When the flashing is finished  
You will be able to see that circuitpython uses the pico as a mountable file system much like a usb drive.
for e.g in Rpi the pico is mounted as /media/CIRCUITPYTHON/
Inside CIRCUITPYTHON you can see the following files:
lib
boot.py
code.py
boot_out.txt
Upload the repos all lib's .py files , boot.py  code.py test.py to the pico.
Run the test.py from tho


## RP-2040-devices
Connect all your sensors to pico and run the host main.py as well as the code.py from pico (to get into listening state)
For pico you need to do it only unless a soft reset key is pressed or hard reset is done.
Disconnect and connecting the pico will automatically run code.py
## VScode Stubs for Circuitpython autocomplete

Download Circuitpython extension from VSCode MArketPlace and install it.Choose Pico as board and you will start seeing autocomplete options.