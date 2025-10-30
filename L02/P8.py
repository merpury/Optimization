"""
Student's Name: นางสาวปริญดา โคตะนิวงษ์
ID: 663040120-8
Diatonic notes on scale.
Print all diatonic notes on scale, given the scale key.
"""

from P8_helper import print_scale # Keep this untouched

# Make the diatonic function work

def diatonic(scale_key):

    # Fix this to work on all keys
    # Hint: recall the triad exercise question
    intervals = [0, 2, 4, 5, 7, 9, 11]

    notes = [(scale_key + i - 1) % 12 + 1 for i in intervals]

    return tuple(notes)
    
# Do not edit below this line.
# ------------------------------------------

if __name__ == "__main__":

    key_of = int(input('Enter the key [1-12]:'))
    k1, k2, k3, k4, k5, k6, k7 = diatonic(key_of)
    print_scale(k1, k2, k3, k4, k5, k6, k7)
    if key_of == 7:
        s = __doc__
        sname = s.split('P20')[0]
        print(sname)

