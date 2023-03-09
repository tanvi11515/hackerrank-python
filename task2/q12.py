n, N = (int(input()), set(map(int, input().split())))
b, B = (int(input()), set(map(int, input().split())))
print(len(N.union(B)))