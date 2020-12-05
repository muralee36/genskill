def tables2(x):
    i=1
    while i<=x:
        for y in range(1,x+1):
            print(i*y,end='\t')
        print('\n')
        i+=1
