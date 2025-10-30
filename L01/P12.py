"""
Given a tennis ball weight in g, top speed in km/h, and court length in m, compute the energy to deliver such a service shot in joules (J) and kilo calories (kcal, which 1 kcal = 4184 J), assuming no air resistance, drag, nor gravity effect.
"""

# Do not edit above this line.
# ------------------------------------------------

def tennis_service(ball_speed, court_length, ball_weight):
    '''
    param:
    ball_speed: top (or final) ball speed in km/h
    court_length: court length in m
    ball_weight: ball weight in g
    return:
    time: time to reach the other end of the court
    Ej:   energy in joules
    Ecal: energy in calories
    '''

    time = 0
    Ej = 0
    Ecal = 0

    # (0) Convert speed and weight to SI units
    # v: speed in m/s
    v = ball_speed * 5/18
    # m: mass in kg
    m = ball_weight /1000
    # distance d: in m
    d = court_length
    # (1) compute the travel time t the ball takes;
    time = (2* d) / v
	#(2) compute an acceleration a, given initial speed (assuming 0) and final speed (assuming at top speed) and time t;
    Ej = 0.5 * m * v * v
	#(3) compute a force f required, then the energy E can be estimated.
    Ecal = Ej / 4.184

    return time, Ej, Ecal


# [!!! Mark 2 !!!]
# Do not edit below this line.
# ------------------------------------------------

if __name__ == '__main__':
    print('Time = %.4f s. Energy = %.2f J = %.2f cal'%tennis_service(
        int(input('Enter the ball speed (km/h):')),
        float(input('Enter the court length (m):')),
        float(input('Enter the ball weight (g):'))))