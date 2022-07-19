# Reference: https://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-12--string-manipulation

def count_substring(string, sub_string):
    instances = 0

    # Finding potentially the first index of sub_string
    start_index = string.find(sub_string)

    # If there is an instance of sub_string that exists
    if(start_index != -1):

        while (start_index + len(sub_string) <= len(string)):
            if (string.find(sub_string, start_index, start_index + len(sub_string)) != -1):
                instances += 1
            start_index += 1

    return instances



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
