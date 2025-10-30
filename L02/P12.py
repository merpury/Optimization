def collect_data():
    observ = []
    counting = []
    while True:
        observ_buffer = input('Observation:')
        if observ_buffer == '':
            break
        observ.append(observ_buffer)

        counting_buffer = int(input('Found:'))
        counting.append(counting_buffer)

    return (observ, counting)