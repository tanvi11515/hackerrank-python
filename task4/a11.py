alphabets = "abcdefghijklmnopqrstuvwxyz"

middle_ini = alphabets[1:size][::-1] + alphabets[0:size]
current_str = ("-").join(list(middle_ini))
res = current_str
for i in range(size-1):
        next_str = current_str.replace(
        current_str[(size*2) - 2 : (size*2) + 2 ], "").center(
            len(current_str),"-")
        res = next_str+"\n"+res+"\n"+next_str
        current_str = next_str
        
print(res)