def power_series():
    x = float(input('x: ')) 
    m = int(input('M: '))   
    
    total = 0
    for i in range(m + 1):
        total += (x ** i) / fact(i)
        
    msg = 's = {:.5f}'.format(total)
    print(msg)

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n-1)
    
if __name__ == '__main__':
    power_series()