if __name__ == '__main__':
    s = input()
    if any(map(str.isalnum,list(s))): print("True") 
    else: print("False")
    if any(map(str.isalpha,list(s))): print("True") 
    else: print("False")
    if any(map(str.isdigit,list(s))): print("True") 
    else: print("False")
    if any(map(str.islower,list(s))): print("True") 
    else: print("False")
    if any(map(str.isupper,list(s))): print("True") 
    else: print("False")
