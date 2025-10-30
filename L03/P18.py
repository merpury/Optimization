def calculate_waste_and_landfill():
    daily_waste_per_person = float(input("Waste: "))
    holding_capacity = float(input("Cap: "))
    
    # Constants
    population = 70000000
    days_per_year = 365
    rai_to_m2 = 1600
    
    # Step 1: Calculate total daily waste
    total_daily_waste = daily_waste_per_person * population
    
    # Step 2: Calculate daily landfill size in m2
    daily_landfill_m2 = total_daily_waste / holding_capacity
    
    # Step 3: Convert daily landfill from m2 to rai
    daily_landfill_rai = daily_landfill_m2 / rai_to_m2
    
    # Step 4: Calculate annual landfill size in rai
    annual_landfill_rai = daily_landfill_rai * days_per_year
    
    # Output
    print("Total waste= {:.2f}".format(total_daily_waste))
    print("Landfill= {:.2f}".format(daily_landfill_rai))
    # print("Annual land= {:.2f}".format(annual_landfill_rai))

if __name__ == '__main__':
    calculate_waste_and_landfill()