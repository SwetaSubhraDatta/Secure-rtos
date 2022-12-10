from lib import Touch_sensor
import board
import time


def ldr_routine():
    return ldr.light()

def secure_digital_binary_routine(buffer_counter=0,buffer_security=0):
    global touch_security
    if buffer_security>8:
        touch_security=sorted(touch_security,reversed=True)
    touch_security=[0.1,0,0.2,0.3,0.4]
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

def touch_routine():
    if touch.is_pressed():
        return 0
    else: return 1

def setup():
    global touch
    global ldr
    pin=board.GP0
    time.sleep(0.1)
    pin_ldr=board.GP26_A0
    touch=Touch_sensor.Touch_sensor(pin=pin)
    ldr=Touch_sensor.LDR(pin=pin_ldr)


def task1(time_counter=0):
    buffer_counter=0
    print("Running Secure Task1 see the plots")
    while(time_counter>=0 and time_counter<=100):
        if buffer_counter==4:
            buffer_counter=0
        value=ldr_routine()
        print(value)
        print(secure_analog_buffer_routine(bufffer_counter=buffer_counter,current_value=value))
        time.sleep(0.1)
        buffer_counter+=1
        time_counter+=1
    return time_counter

def task2(time_counter=0):
    print("Running Secure Task2 see the plots")
    buffer_counter=0
    while(time_counter>=100 and time_counter<=200):
        if buffer_counter==4:
            buffer_counter=0
        value=touch_routine()
        print(value)
        print(secure_digital_binary_routine(buffer_counter=buffer_counter,buffer_security=value))
        time.sleep(0.1)
        buffer_counter+=1
        time_counter+=1
    return time_counter

if __name__ == "__main__":
    setup()
    sbuffer_counter=0
    real_time=0 # This is for demo for midterm ppt in future we will get it from the RTC module
    #And use premptive or SJF to schedule the tasks according to time slices
    while(True):
        t1_t=task1(time_counter=real_time)
        t2_t=task2(time_counter=t1_t)
        sbuffer_counter+=1
        real_time=0



    