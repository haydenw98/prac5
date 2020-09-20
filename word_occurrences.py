word_to_count = {}
words = []
text = input("Text: ")
words = text.split()
print(words)
for x in words:
    amount = word_to_count.get(x, 0)
    word_to_count[x] = amount + 1
words = list(word_to_count.keys())
words.sort()
for word in words:
    print("{} : {}".format(word, word_to_count[word]))
