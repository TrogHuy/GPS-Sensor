# app.py
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)
import time
import counterfit_shims_serial
from simple_gps_decoder import decode_gps

serial = counterfit_shims_serial.Serial('/dev/ttyAMA0')

print("Simple GPS reader running on http://127.0.0.1:5000")

while True:
    line = serial.readline().decode('utf-8').strip()
    
    if line:
        print(f"Raw NMEA: {line}")
        
        # Try to decode the GPS data
        gps_data = decode_gps(line)
        
        # Print decoded data if available
        if gps_data:
            lat = gps_data['latitude']
            lon = gps_data['longitude']
            sats = gps_data['satellites']
            
            print(f"Latitude: {lat}")
            print(f"Longitude: {lon}")
            print(f"Satellites: {sats}")
            print("-" * 30)
    
    time.sleep(1)