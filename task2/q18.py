n = int(input())

for _ in range(n):
    
    input()
    a = set(input().split())
    input()
    b = set(input().split())

    print(a.issubset(b))