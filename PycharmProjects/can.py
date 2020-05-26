from __future__ import print_function
import can

def send_one():


bus = can.interface.Bus()
bus= can.interface.Bus(bustype='vector', app_name='CANalyzer',channel=0, bitrate=250000)
msg =can.Message(arbirtration_id=    ,data=[], is_extended_id=True)

try:
    bus.send(msg)
    print("message sent on {}".format(bus.channel_info))
except can.CanERROR:
    print("Message Not sent")

if __name__ == '__main__':
    send_one()