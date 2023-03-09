def solve(s):
    found = True
    st = ''
    for i in s:
        if found == True:
            st += i.upper()
            found = False
        else:
            st += i
        if i == ' ':
            found = True
    return st