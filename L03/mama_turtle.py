"""
To use turtle to draw a road scene.
"""

try:
    import turtle
except ImportError:
    # print('Import Error: no turtle installed')
    pass

import math


def find_pol(b_point, e_point, rad=False):
    mag = math.sqrt((b_point[0] - e_point[0]) ** 2 + \
                    (b_point[1] - e_point[1]) ** 2)

    dx = e_point[0] - b_point[0]
    dy = e_point[1] - b_point[1]

    theta = math.pi / 2
    if dx == 0:
        if dy < 0:
            theta = -math.pi / 2
    else:
        theta = math.atan(dy / dx)

    if dx < 0:
        theta += math.pi

    if rad:
        return mag, theta

    deg = theta / math.pi * 180

    return mag, deg


def find_depth_parts(d, h, epsilon, num_div_parts):
    '''
    :param d: depth spacing
    :param h: view height
    :parame epsilon: projection screen depth
        e.g., epsilon = 2*d (set it relative to d)
        large epsilon --> more evenly spacing
        small epsilon --> depth spacing reduces fast
    :return:
    '''

    parts = []
    hn_prev = 0
    for i in range(num_div_parts + 1):
        nd = (i + 1) * d
        hn = h * nd / (nd + epsilon)
        parts.append(hn - hn_prev)
        hn_prev = hn

    parts = parts[1:]

    return parts


class road:
    def __init__(self, vx=0, vy=75, road_offset=0,
               lamp_height=40):
        # Vanishing point
        self.vx = vx
        self.vy = vy

        # Horizontal line
        self.h_line = vy

        # Draw canvas
        self.left = -200
        self.right = 200
        self.top = 150
        self.bottom = -100

        # Road starting location
        self.road_offset = road_offset
        self.road_left_edge = -100 + road_offset
        self.road_right_edge = 100 + road_offset

        # Road marks
        self.road_mark_x = (self.road_left_edge + self.road_right_edge)/2
        self.road_mark_length = 1
        self.num_marks = 9
        self.road_mark_width = 5

        # Lamp posts
        self.num_lamp_posts = 5
        self.lamp_height=lamp_height

        turtle.setup(self.right-self.left,
                     self.top-self.bottom)

        self.t = turtle.Turtle()
        self.t.hideturtle()

    def draw_road(self):
        # Draw the vanishing point
        self.t.up()
        self.t.goto(self.vx, self.vy)
        self.t.color('red')
        self.t.down()
        self.t.circle(3)

        # Draw the horizontal line
        self.t.up()
        self.t.goto(self.left, self.h_line)
        self.t.color('blue')
        self.t.down()
        self.t.goto(self.right, self.h_line)

        # Draw road
        self.t.up()
        self.t.goto(self.road_left_edge, self.bottom)
        self.t.color('gray')
        self.t.down()
        self.t.color('black', 'gray')
        self.t.begin_fill()
        self.t.goto(self.vx, self.vy)
        self.t.goto(self.road_right_edge, self.bottom)
        self.t.goto(self.road_left_edge, self.bottom)
        self.t.end_fill()

        # Calculate depth spacing
        b_point = (self.road_mark_x, self.bottom)
        e_point = (self.vx, self.vy)
        total_length, tilt_angle = find_pol(b_point, e_point)
        d = total_length / self.num_marks
        h = 10  # guess viewer's height
        epsilon = 2 * d
        road_parts = find_depth_parts(d, h, epsilon, self.num_marks)

        # Draw road marks
        self.t.up()
        line_width = self.t.width()
        self.t.width(self.road_mark_width)
        self.t.goto(self.road_mark_x, self.bottom)
        self.t.color('white')
        self.t.down()

        # print(self.t.heading())
        # print(self.t.pos())
        self.t.setheading(tilt_angle)

        for p in road_parts:
            plength = p / sum(road_parts) * total_length
            self.t.fd(plength)
            if self.t.isdown():
                self.t.up()
            else:
                self.t.down()

        self.t.width(line_width)

    def _draw_posts(self, height):
        old_width = self.t.width()
        old_pos = self.t.pos()
        self.t.width(5)
        self.t.color('brown')
        self.t.setheading(90)
        self.t.down()
        self.t.fd(height)
        self.t.width(old_width)
        self.t.up()
        self.t.goto(old_pos[0], old_pos[1])

    def draw_lamp_posts(self, lamp_height_fn):

        ###################################
        ## Draw lamp posts
        ###################################
        b_point = (self.road_right_edge, self.bottom)
        e_point = (self.vx, self.vy)
        total_length, tilt_angle = find_pol(b_point, e_point)
        d = total_length / self.num_lamp_posts
        h = 1000  # guess viewer's height
        # epsilon = 10*d # quite even
        epsilon = d
        # epsilon = 0.1*d # depth is emphasized

        lamp_parts = find_depth_parts(d, h, epsilon, self.num_lamp_posts)

        self.t.up()
        self.t.goto(self.road_right_edge, self.bottom)

        d = 0
        for p in lamp_parts:
            height = lamp_height_fn(self.vx, self.vy,
                                     self.road_right_edge,
                                     self.bottom,
                                     self.lamp_height, d)

            self._draw_posts(height)
            plength = p / sum(lamp_parts) * total_length
            self.t.setheading(tilt_angle)
            self.t.fd(plength)
            d += plength


if __name__ == '__main__':
    r = road()
    r.draw_road()

    fn = lambda vx, vy, x, y, height, dist: 50

    r.draw_lamp_posts(fn)

    input('enter to exit')