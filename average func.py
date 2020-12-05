def average_func(*args):
    sum=0
    for x in args:
        sum+=x
    l=len(args)
    return sum/l

print(average_func(20, 30))
