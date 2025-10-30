def earthquake(events):
    for event in events:
        mag = event[1]
        energy = 10**(4.8 + 1.5*mag)
        event.append(energy)
    return events