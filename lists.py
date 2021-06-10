if __name__ == '__main__':
    commands = []
    arr = []
    all_arrs = []   # List of items to print after all these computations
    N = int(input())
    
    # Inputting commands
    for i in range(N):
        commands.append(input())
    
    # Reading commands[] and modifying lists accordingly
    for statement in commands:
        param = statement.split()   # split() used to seperate commands and parameters
        
        if param[0] == "insert":
            arr.insert(int(param[1]), int(param[2]))
        elif param[0] == "print":
            all_arrs.append(list(arr))
        elif param[0] == "remove":
            arr.remove(int(param[1]))
        elif param[0] == "append":
            arr.append(int(param[1]))
        elif param[0] == "sort":
            arr.sort()
        elif param[0] == "pop":
            arr.pop()
        elif param[0] == "reverse":
            arr.reverse()

    for _ in all_arrs:
        print(_)