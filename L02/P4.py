def martian_botanist(sols, daily_consumption, production):
    total_potato_needed = sols * daily_consumption
    planting_area = total_potato_needed / production
    
    return planting_area