def fuzzbuzz(x):
    for i in range(1,x+1):
        if i%15==0:
            print('fuzzbuzz')
        elif i%3==0:
            print('fuzz')
        elif i%5==0:
            print('buzz')
        else:
            print(i)