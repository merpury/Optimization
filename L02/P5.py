def dec_to_hex(num):
    if num >= 10:
        if num == 10:
            return 'a'
        elif num == 11:
            return 'b'
        elif num == 12:
            return 'c'
        elif num == 13:
            return 'd'
        elif num == 14:
            return 'e'
        elif num == 15:
            return 'f'
        else:
            return -1
    return str(num)

def numsys(dec_num):
    binary_divider = 2
    binary_result = ""

    hex_divider = 16
    hex_result = ""

    binary_divided = dec_num
    hex_divided = dec_num

    while True:
        binary_buffer = binary_divided % binary_divider
        binary_divided = binary_divided // binary_divider
        binary_result += str(binary_buffer)

        if binary_divided == 0:
            break

    while True:
        hex_buffer = hex_divided % hex_divider
        hex_divided = hex_divided // hex_divider
        hex_result += dec_to_hex(hex_buffer)

        if hex_divided == 0:
            break

    binary_result = "0b" + binary_result[::-1]
    hex_result = "0x" + hex_result[::-1]

    return (binary_result, hex_result)