import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    cnt = 0
    for i in range(0, len(seq) - 4):
        matched = True
        for j in range(i, i + 5):
            if seq[j] == 0:
                matched = False
                break
        if matched:
            cnt += 1
    return cnt

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
