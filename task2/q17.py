k = int(input())
frequency_map = {}
for i in map(int, input().split()):
    if i in frequency_map:
        frequency_map[i] += 1
    else:
        frequency_map[i] = 1
for i in frequency_map:
    if frequency_map[i] == 1:
        print(i)