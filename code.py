def carFleet(target, position, speed):
    if not position:
        return 0
    
    cars = sorted(zip(position, speed), key=lambda x: -x[0])
    max_time = 0
    fleet_count = 0
    
    for p, s in cars:
        time = (target - p) / s
        if time > max_time:
            fleet_count += 1
            max_time = time
    
    return fleet_count