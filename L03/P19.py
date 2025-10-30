usartdiv = (16 * (10 ** 6)) / (8 * 2 * 115200)
msg = '{:.4f}'.format(usartdiv)
print(msg)
# print(round(usartdiv * 16))