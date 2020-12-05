def biggest_smallest(*args):
    big=args[0]
    small=args[0]
    for i in args:
        if i>big:
            big=i
        if i<small:
            small=i
    return (big,small)