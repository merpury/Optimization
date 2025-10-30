import math

if __name__ == '__main__' :
    V = float(input('Plane speed (mph):'))
    T = float(input('Interval between crash and the last contact (h):'))

    r = V * T
    Area = math.pi*r*r
    thailand = 198120
    Area_perspective = Area/thailand

    report = "Search area = {:,.2f} sq.mi."
    print(report.format(Area))

    perspactive = "That's {:,.2f} time(s) the size of Thailand."
    print(perspactive.format(Area_perspective))
