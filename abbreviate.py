def abbreviate(s):
    new_s=s.split()
    abb=[]
    for i in new_s:
        if i[0].isupper():
            abb.append(i[0])
    res=''.join(abb)
    print(res)