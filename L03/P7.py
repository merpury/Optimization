import math

def Hipparchus(do_km, theta_m_deg):
    empty_list = []
    for offset in [-0.01, 0, 0.01]:
        current_angle = theta_m_deg + offset
        distance_to_moon = (do_km / 2) * math.tan(math.radians(current_angle))
        empty_list.append(distance_to_moon)
    
    empty_list.sort()
    return empty_list[1], empty_list[0], empty_list[2]

def Aristarchus(dm_km, theta_s_deg):
    Ds = dm_km / math.tan(math.radians(theta_s_deg))
    
    Ds_lower = dm_km / math.tan(math.radians(theta_s_deg + 0.01))
    Ds_upper = dm_km / math.tan(math.radians(theta_s_deg - 0.01))
    
    Dsl, Dsu = sorted((Ds_lower, Ds_upper))
    return Ds, Dsl, Dsu

# res = Hipparchus(400, 89.97)
# print('Hipparchus:{:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res))
# res = Aristarchus(381972, 0.15)
# print('Aristarchus: {:,.2f} km; [{:.0f} , {:.0f}] if 0.01 deg off'.format(*res))