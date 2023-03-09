n,m = [int(x) for x in input().split()]
p = '.|.'

j=0
for i in range(0,n):
    # print(i)
    if i<n//2:
        print(((j*2+1)*p).center(m, '-'))
        j=j+1
    elif i==n//2:
        print('WELCOME'.center(m, '-'))
    else:
        j=j-1
        print(((j*2+1)*p).center(m, '-'))