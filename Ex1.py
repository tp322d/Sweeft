from collections import Counter


n = int(input())
words = []
for i in range(n):
    words.append(input())
words_counter = Counter(words)
print(len(words_counter))
for i in words_counter.values():
    print(i, end=' ')
