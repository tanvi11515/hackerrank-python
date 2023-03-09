A = set(input().split())
sup = True
for _ in range(int(input())):
    B = set(input().split())
    if not (A > B):
        sup = False
        break
print (sup)
    