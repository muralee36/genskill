from random import random
def est_pi():
    m=0
    n=0
    total=100000
    while m<=total:
        x2=random()**2
        y2=random()**2
        m+=1
        if x2+y2<1:
            n+=1
    pi_est=4*(n/total)
    return pi_est
