number = int(input())
lst = []
for i in range(number):
    enter = input()
    lst.append(enter)
    
resultado = len(set(lst))

print(resultado)