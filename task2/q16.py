n = int(input())
A = set(map(int, input().split()))
N = int(input())
operations = []
for i in range(N):
    op, dummy = input().split()
    numbers = set(map(int, input().split()))
    operations.append((op, numbers))
for op, numbers in operations:
    if(op == 'intersection_update'):
        A &= numbers
    if(op == 'symmetric_difference_update'):
        A ^= numbers
    if(op == 'difference_update'):
        A -= numbers
    if(op == 'update'):
        A |= numbers
print(sum(A))