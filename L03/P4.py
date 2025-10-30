def krill_consumption(feeding, whales):
    total = 0
    for whale_type, count in whales.items():
        if whale_type in feeding:
            total += feeding[whale_type] * count
    return total

