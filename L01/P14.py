"""
Given a rain density in mm/h and an area in rai,
write a program to calculate the amount of rain water in L.
The program, named rain_water, takes 3 arguments:
an area of the field (in rai, as a number either in integer or float),
a rain density (in mm/h, as a floating-point number),
and a number of raining hours.
Then, calculate the amount of water and return it.
"""

# Do not edit above this line.
# ------------------------------------------------


# ... Your function will be here
def rain_water(area1,rain_density,time):
    # :param:
    # * an area of the field in rai
    # * rain density in mm/h
    # * a number of raining hours
    # :return:
    # * an amount of water in L

    # Hint:
    # (1) Find an area in sq.m.: 1 rai = 1600 sq.m.
    area_sqm = area1 * 1600
    # (2) Find rainfall in mm: (rain in mm) = (density in mm / h) *(duration in h).
    rainfall = rain_density * time
    # (3) Find water in L: water in L = (rain in mm) * (area in sq.m.).
    water = rainfall * area_sqm

    return water

# [!!! Mark 2 !!!]
# Do not edit below this line.
# ------------------------------------------------

if __name__ == '__main__':
    area = input('Area name:')
    print('{}: rain water = {:,.2f} L'.format(area, rain_water(
        float(input('Size of the area (in rai):')),
        float(input('The area rain density (in mm/h):')),
        float(input('The number of raining hours:'))
    )))