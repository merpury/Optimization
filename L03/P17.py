def half_life():
    
    ratio = float(input('ratio: '))
    sen = float(input('sensitivity: '))
    i = 0
    while True:
        current_ratio = ratio / (2 ** i)
        print('Year {}: ratio = {}'.format(5730 * i, current_ratio))
        if abs(current_ratio - sen) <= sen or current_ratio <= sen:
            break
        
        i += 1

if __name__ in '__main__':
    half_life()