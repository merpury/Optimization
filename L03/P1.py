import math

def cos_sim(A, B):
    dot_product = sum(a * b for a, b in zip(A, B))
    magnitude_A = math.sqrt(sum(a ** 2 for a in A))
    magnitude_B = math.sqrt(sum(b ** 2 for b in B))
    if magnitude_A == 0 or magnitude_B == 0:
        return 0
    return dot_product / (magnitude_A * magnitude_B)

