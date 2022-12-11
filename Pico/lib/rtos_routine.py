from lib.sensors import Touch_sensor
from lib.sensors import LDR
import board
import time


def ldr_routine(ldr):
    return ldr.light()

def touch_routine(touch):
    if touch.is_pressed():
        return 0
    else: return 1


def secure_digital_binary_routine(buffer_counter=0,buffer_security=0):
    global touch_security
    if buffer_security>8:
        touch_security=sorted(touch_security,reversed=True)
    touch_security=[19,8,7,6,5]
    return touch_security[buffer_counter]
    

def secure_analog_buffer_routine(bufffer_counter=0,current_value=0):
    global buffer_security
    buffer_security=[600.00,700.00,640.00,750.00,650.00]
    if current_value>800 and current_value<900:
        for i in range(len(buffer_security)):
            buffer_security[i]+=200
    elif current_value>900 and current_value<1000:
        for i in range(len(buffer_security)):
            buffer_security[i]+=300
    elif current_value>1000 and current_value<1100:
        for i in range(len(buffer_security)):
            buffer_security[i]+=400
    elif current_value>1100 and current_value<1200:
        for i in range(len(buffer_security)):
            buffer_security[i]+=500
    elif current_value>0 and current_value<100:
        for i in range(len(buffer_security)):
            buffer_security[i]-=400
    elif current_value>100 and current_value<200:
        for i in range(len(buffer_security)):
            buffer_security[i]-=300
    elif current_value>200 and current_value<300:
        for i in range(len(buffer_security)):
            buffer_security[i]-=200
    else:
        buffer_security=buffer_security
    return buffer_security[bufffer_counter]




def task2(time_counter,ldr_sensor,dout):
    buffer_counter=0
    print("Running Secure Task1 see the plots")
    while(time_counter>=0 and time_counter<=8): #Hardcoding timeslices for now later will get from the real time clock/Systicks
        if buffer_counter==4:
            buffer_counter=0
        value=ldr_routine(ldr_sensor)
        dout["Task2"]["values"].append(value)
        dout["Task2"]["values"].append(secure_analog_buffer_routine(bufffer_counter=buffer_counter,current_value=value))
        time.sleep(0.1)
        buffer_counter+=1
        time_counter+=1
    return time_counter

def task1(time_counter,touch_sensor,dout):  ##Need to modify the counter system
    print("Running Secure Task1 see the plots")
    buffer_counter=0
    while(time_counter>=0 and time_counter<=8):
        if buffer_counter==4:
            buffer_counter=0
        value=touch_routine(touch_sensor)
        dout["Task1"]["values"].append(value)
        dout["Task1"]["values"].append(secure_digital_binary_routine(buffer_counter=buffer_counter,buffer_security=value))
        time.sleep(0.1)
        buffer_counter+=1
        time_counter+=1
    return time_counter
