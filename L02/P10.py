def clock_to_degrees(time_str):

    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    
    degrees = (hours * 30 + minutes * 0.5) % 360
    return degrees

def sailor_mate(wind_direction, desired_direction):
    wind_deg = clock_to_degrees(wind_direction)
    desired_deg = clock_to_degrees(desired_direction)
    
    relative_angle = (desired_deg - wind_deg + 360) % 360
    
    if relative_angle == 0:
        return "run"  
    elif 0 < relative_angle < 90:
        return "starboard broad reach"  
    elif relative_angle == 90:
        return "starboard beam reach"  
    elif 90 < relative_angle < 135:
        return "starboard close hauled"  
    elif 135 <= relative_angle <= 225:
        return "tacking" 
    elif 225 < relative_angle < 270:
        return "port close hauled"  
    elif relative_angle == 270:
        return "port beam reach"  
    elif 270 < relative_angle < 360:
        return "port broad reach"
    
    return "unknown" 

# Test examples
if __name__ == '__main__':
    # Example 1
    r = sailor_mate("9:00", "12:00")
    print("9:00", "12:00", r)
    
    ticks = ["12:00", "1:30", "1:31", "2:59", "3:00", 
             "3:01", "5:59", "6:00", "6:01", "8:59", "9:00", "9:01", 
             "10:27", "10:30"]
    for b in ticks:
        r = sailor_mate("6:00", b)
        print("6:00", b, r)