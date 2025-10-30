from mama_turtle import road, find_pol
import math

def brunelleschi_lamp(vx, vy, x, y, height, d, logfile='log.txt'):
    '''
    :param vx, vy: vanishing point coordinate
    :param x, y: reference lamp coordinate
    :param height: reference lamp height
    :param d: distance from ref to the lamp under question
                in direction toward the vanishing point
    '''

    # Write your code here!

    # Hint:
    # 1. find_pol can help on L and beta
    # 2. find_pol can help on phi as well
    # 3. H = (L - d) sin beta
    # 4. tau = (L - d) cos beta
    # 5. (H - h')/tau = tan phi

    # Dummies
    # L, beta = find_pol([vx, vy], [x, y], rad=True)
    L, beta = find_pol([vx, vy], [x, y], rad=True)
    
    beta = abs(beta)
    
    H = (L - d) * math.sin(beta)
    tau = (L - d) * math.cos(beta)
    # print(tau)
    # _, phi = find_pol([vx, vy], [x, y + height], rad=True)
    _, phi = find_pol([x, y + height], [vx, vy])
 
    phi = math.radians(180 - phi)      
    # phi = abs(phi)
    
    hprime = H - tau * math.tan(phi)

    inp_msg = "Input: vx={:.2f}, vy={:.2f}, x={:.2f}, y={:.2f}, " + \
              "height={:.2f}, d={:.2f}.\n"
    inp_msg = inp_msg.format(vx, vy, x, y, height, d)

    calc_msg = "Calc: L = {:.2f}, beta = {:.2f}, " + \
        "H = {:.2f}, tau = {:.2f}, phi = {:.2f}, " + \
        "h' = {:.2f}.\n"
    calc_msg = calc_msg.format(L, beta, H, tau, phi, hprime)
    with open(logfile, 'a') as f:
        f.write(inp_msg)
        f.write(calc_msg)


    return hprime


if __name__ == '__main__':
    r = road()
    # r = road(vx=50, vy=75, road_offset=-30,
    #            lamp_height=80)
    # r = road(vx=-80, vy=0, road_offset=100,
    #            lamp_height=50)
    # r = road(vx=-120, vy=-50, road_offset=110,
    #            lamp_height=60)
    # r = road(vx=0, vy=120, road_offset=0,
    #            lamp_height=60)

    #r.draw_road()
    #r.draw_lamp_posts(brunelleschi_lamp)

    #input('enter to exit')