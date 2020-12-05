def biggest(*args):
    big=args[0]
    for i in args:
        if i>big:
            big=i
    return big