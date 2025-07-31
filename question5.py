words = ["apple", "banana", "cherry", "date", "elderberry"]

for word in words:
    if (len(word) % 2) != 0:  # Check if the length of the word is odd
        print(word)