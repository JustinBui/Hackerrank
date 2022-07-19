from collections import OrderedDict

if __name__ == "__main__":
    unique_words = OrderedDict()

    # Inputs
    for _ in range(int(input())):
        word = input()
        # If the word does not exist, set it to 0
        unique_words.setdefault(word, 0)
        unique_words[word] += 1
