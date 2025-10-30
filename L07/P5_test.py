from P5 import P5_wer
if __name__ == '__main__':
    wer, n = P5_wer("grit", "greet")
    print("wer = {}, n = {}".format(wer, n))