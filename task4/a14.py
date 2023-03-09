from textwrap import wrap

def merge_the_tools(string, k):
    ls = wrap(string, k)
    new_ls = []
    for x in ls:
        result = x[0]
        for i in range(1,len(x)):
            if x[i] not in result:
                result += x[i]
            else: 
                continue
        print(result)
 
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)