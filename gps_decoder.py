# simple_gps_decoder.py

def decode_gps(nmea_sentence):
    # Check if it's a GGA sentence (contains the info we want)
    if not nmea_sentence.startswith('$GPGGA') and not nmea_sentence.startswith('$GNGGA'):
        return None
    
    # Split the sentence into parts
    parts = nmea_sentence.split(',')
    
    # Initialize result
    result = {
        'latitude': None,
        'longitude': None,
        'satellites': None
    }
    
    try:
        # Extract latitude (format: DDMM.MMMMM)
        if len(parts) > 2 and parts[2] and parts[3]:
            lat_dm = float(parts[2])
            lat_direction = parts[3]
            
            # Convert to decimal degrees
            lat_deg = int(lat_dm / 100)
            lat_min = lat_dm - (lat_deg * 100)
            latitude = lat_deg + (lat_min / 60)
            
            # Apply direction
            if lat_direction == 'S':
                latitude = -latitude
                
            result['latitude'] = latitude
        
        # Extract longitude (format: DDDMM.MMMMM)
        if len(parts) > 4 and parts[4] and parts[5]:
            lon_dm = float(parts[4])
            lon_direction = parts[5]
            
            # Convert to decimal degrees
            lon_deg = int(lon_dm / 100)
            lon_min = lon_dm - (lon_deg * 100)
            longitude = lon_deg + (lon_min / 60)
            
            # Apply direction
            if lon_direction == 'W':
                longitude = -longitude
                
            result['longitude'] = longitude
        
        # Extract number of satellites
        if len(parts) > 7 and parts[7]:
            result['satellites'] = int(parts[7])
            
    except (ValueError, IndexError):
        # If parsing fails, return what we have so far
        pass
    
    return result