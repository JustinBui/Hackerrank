# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    # Taking input of first list
    size_1 = int(input())
    l1 = input()
    l1 = l1.split()
    l1 = list(map(int, l1))

    set_1 = set()

    # Inputting contents into first set from first  list
    for _ in range(size_1):
        set_1.add(l1[_])

    # Taking input from second list
    size_2 = int(input())
    l2 = input()
    l2  =l2.split()
    l2 = list(map(int, l2))

    set_2 = set()

    # Inputting contents into second set from second list
    for _ in range(size_2):
        set_2.add(l2[_])

    
    s = set_1 ^ set_2   # Finding symmetric difference
    s = sorted(list(s))         # Converting symmetric difference into printable list

    # Printing list contents
    for _ in range(len(s)):
        print(s[_])
