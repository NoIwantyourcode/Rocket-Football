import time
import board
import pwmio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

FREQ=20000
SPEED=0.8

in1=pwmio.PWMOut(board.P0_09,frequency=FREQ,duty_cycle=0)
in2=pwmio.PWMOut(board.P0_10,frequency=FREQ,duty_cycle=0)
in3=pwmio.PWMOut(board.P1_11,frequency=FREQ,duty_cycle=0)
in4=pwmio.PWMOut(board.P1_13,frequency=FREQ,duty_cycle=0)

def pwm(x): return int(max(0,min(1,x))*65535)
def stop():
    for p in (in1,in2,in3,in4): p.duty_cycle=0
def left(sp):
    in1.duty_cycle=pwm(sp); in2.duty_cycle=0
def left_rev(sp):
    in1.duty_cycle=0; in2.duty_cycle=pwm(sp)
def right(sp):
    in3.duty_cycle=pwm(sp); in4.duty_cycle=0
def right_rev(sp):
    in3.duty_cycle=0; in4.duty_cycle=pwm(sp)

ble=BLERadio(); ble.name="RC-CAR"
uart=UARTService()
adv=ProvideServicesAdvertisement(uart)

while True:
    ble.start_advertising(adv)
    while not ble.connected: pass
    ble.stop_advertising()
    while ble.connected:
        if uart.in_waiting:
            c=uart.read(1)
            if c==b'F':
                left(SPEED); right(SPEED)
            elif c==b'B':
                left_rev(SPEED); right_rev(SPEED)
            elif c==b'L':
                left_rev(SPEED); right(SPEED)
            elif c==b'R':
                left(SPEED); right_rev(SPEED)
            else:
                stop()
        time.sleep(0.01)
    stop()
