if __name__ == '__main__':
    N = int(input())
    resList = []
    for i in range(N):
        command = input().split()
        if command[0] == "insert":
            resList.insert(int(command[1]),int(command[2]))
        
        elif command[0] == "remove":
            resList.remove(int(command[1]))
        
        elif command[0] == "append":
            resList.append(int(command[1]))
            
        elif command[0] == "sort":
            resList.sort()
        
        elif command[0] == "pop":
            resList.pop()
        
        elif command[0] == "reverse":
            resList.reverse()
        
        else:
            print(resList)