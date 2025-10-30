def survive_mars(area_m2, depth_cm):
    depth_m = depth_cm / 100
    soil_volume = area_m2 * depth_m
    water_required = soil_volume * 40
    
    return water_required