
if __name__ == '__main__':
    n = int(input())
    s = ''
    
# Top cone

for i in range(1,n*2,2):
    s = s + (i * 'H').center(n * 2 - 1 , " ") + '\n'
    
# Top Square

s1 = (n * 'H').center(n * 2 - 1 , " ") + (n * 2 + 1) * " "

for i in range(n + 1):
    s = s + (2 * s1) + '\n'

# Middle line

s2 = (n * 5 * 'H').center(n * 6 - 1 , " ")

for i in range(0 , n , 2):
    s = s + s2 + '\n'

# Bottom square

s3 = (n * 'H').center(n * 2 - 1 , " ") + (n * 2 + 1) * " "

for i in range(n + 1):
    s = s + (2 * s3) + '\n'

# Bottom cone

for i in range(n * 2 - 1 , 0 , -2):
    s = s + (n * 4) * ' ' + (i * 'H').center(n * 2 - 1) + '\n'

print(s)