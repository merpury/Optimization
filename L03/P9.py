"""
Write a function named sweet to take 2 filenames:
one is for a sweetness table and
another one is for sweeteners in a drink.
The function calculates estimated sweetness of the drink
comparable to 10% sucrose solution,
and appends its calculate to the end of the second file
---the drink-sweetener file.
"""

def sweet(fsweet, fdrink):

    # Retrieve sweetness dict
    sweetness = {}
    with open(fsweet, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or '=' not in line:
                continue
            sweetener, value = line.split('=')
            sweetness[sweetener.strip()] = float(value.strip())
    
    # Optional: check if we read it correctly
    # print(sweetness)

    # Step 2: Read drink file and calculate estimated sweetness
    sweet_sum = 0
    with open(fdrink, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # assume each line contains the sweetener name and amount (optional)
            # e.g., "Aspartame=2.5"
            if '=' in line:
                name, amount = line.split('=')
                name = name.strip()
                amount = float(amount.strip())
            else:
                name = line.strip()
                amount = 1.0  # default if no amount specified

            # add to total sweetness if known
            if name in sweetness:
                sweet_sum += sweetness[name] * amount
            else:
                print(f"{name}")

    # Step 3: Append result to the drink file
    msg = "\nSweet as {:.1f}% sucrose solution".format(sweet_sum)
    with open(fdrink, 'a') as f:
        f.write(msg)


# if __name__ == '__main__':
    # sweet('sweetness1.txt', 'CocaPanda.txt')