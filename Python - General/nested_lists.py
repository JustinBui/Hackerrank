if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key = lambda x: x[1])
    
    lowest = students[0][1]
    new_list = []

    # Getting the second lowest score
    for i in range(1, len(students)):
        if (lowest < students[i][1]):
            second_lowest = students[i][1]
            break
    
    # Getting any pair [student, score] that has score
    # equal to second lowest
    for i in range(1, len(students)):
        if (students[i][1] == second_lowest):
            new_list.append(students[i])

    new_list = sorted(new_list, key = lambda x: x[0])

    # Printing the names of second lowest in alphabetical order
    for i in range(new_list):
        print(new_list[i][0])
