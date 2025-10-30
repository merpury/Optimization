"""
Given a note index (1-12), print the note name (C, C#, D, ..., B)
Major scales:   C, D, E, F, G,  A,  B; Db, Eb, Ab, Bb
                1  3  5  6  8  10  12   2   4   9  11
                Major scale of key 7 (F# or Gb) will crash either E# or Cb
"""

def i2n(idx, flat=False):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    flat_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    ns = notes
    if flat:
        ns = flat_notes

    return ns[idx-1]

def print_scale(*args):
    k = args[0]
    print('Diatonic notes in the key of',
          i2n(k, flat=True), '(', k, ')')

    dnotes = []
    if k in [2, 4, 6, 9, 11]:
        dnotes = [i2n(v, flat=True) for v in args]
    else:
        dnotes = [i2n(v) for v in args]

    #print(dnotes)
    #print(args)
    print('%2s %2s %2s %2s %2s %2s %2s'%tuple(dnotes))
    print('%2s %2s %2s %2s %2s %2s %2s'%(args))


if __name__ == '__main__':
    for i in range(12):
        print(i2n(i+1), end=' ')

    print()
    for i in range(12):
        print(i2n(i+1, flat=True), end=' ')

    print()
    print_scale(1, 3, 5, 6, 8, 10, 12)