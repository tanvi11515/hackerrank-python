mylist1 = []
mylist2 = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    mylist1.append([name,score])
    mylist2.append(score)

f_low = min(mylist2)

cnt = mylist2.count(f_low)

while cnt>0:
    mylist2.remove(f_low)
    cnt = cnt-1


# finding new min element 

new_min = min(mylist2)

mylist1.sort()

for student in mylist1:
    if student[1] == new_min:
        print(student[0])