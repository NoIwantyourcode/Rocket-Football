import time,board,digitalio
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

pins=[board.P0_09,board.P0_10,board.P1_11,board.P1_13]
cmds=[b'F',b'B',b'L',b'R']
buttons=[]
for p in pins:
    b=digitalio.DigitalInOut(p)
    b.direction=digitalio.Direction.INPUT
    b.pull=digitalio.Pull.UP
    buttons.append(b)

ble=BLERadio()
uart=None
print("Scanning...")
while uart is None:
    for adv in ble.start_scan(ProvideServicesAdvertisement,timeout=2):
        if UARTService in adv.services:
            conn=ble.connect(adv)
            uart=conn[UARTService]
            break
    ble.stop_scan()
print("Connected")

last=None
while True:
    cmd=b'S'
    for i,b in enumerate(buttons):
        if not b.value:
            cmd=cmds[i]
            break
    if cmd!=last:
        uart.write(cmd)
        last=cmd
    if not ble.connected:
        raise SystemExit("Disconnected; reset to reconnect")
    time.sleep(0.02)
