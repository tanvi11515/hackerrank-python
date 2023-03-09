import textwrap

def wrap(string, max_width):
    w=textwrap.wrap(string,max_width)
    for i in range(0,len(w)-1):
        print(w[i])
    return(w[i+1])
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)