def panagram(x):
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i not in x.lower():
            return False
    return True