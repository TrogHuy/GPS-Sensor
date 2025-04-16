# decode_gps.py
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

import counterfit_shims_serial
import pynmea2
import time

serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

def decode_gps_data(line):
    try:
        msg = pynmea2.parse(line)
        if isinstance(msg, pynmea2.types.talker.GGA):  # GPS fix data
            print(f"Time: {msg.timestamp}, Lat: {msg.latitude} {msg.lat_dir}, Lon: {msg.longitude} {msg.lon_dir}, Satellites: {msg.num_sats}")
        elif isinstance(msg, pynmea2.types.talker.RMC):  # Recommended Minimum Navigation Information
            print(f"Time: {msg.timestamp}, Status: {msg.status}, Lat: {msg.latitude}, Lon: {msg.longitude}, Speed: {msg.spd_over_grnd}")
        else:
            print("Parsed:", msg)
    except pynmea2.ParseError:
        print("Could not parse line:", line.rstrip())

print("Decoder running...")

while True:
    line = serial.readline().decode('utf-8').strip()
    if line:
        decode_gps_data(line)
    time.sleep(0.1)
