import numpy as np
from scipy.spatial import distance
import re
from collections import defaultdict

text = open('sentences.txt', 'r')
sentences = list(map(lambda s: s.lower(), text.readlines()))
text.close()

sentences = list(map(lambda sentence: re.split('[^a-z]', sentence), sentences))
for sentence in sentences:
    i = 0
    while i < len(sentence):
        if sentence[i].isalpha():
            i += 1
        else:
            del sentence[i]

words = dict()
ind = 0
for sentence in sentences:
    for word in sentence:
        if not word in words:
            words[word] = ind
            ind += 1

n = len(sentences)
counts = [defaultdict(int) for i in range(n)]
for i in range(n):
    for word in sentences[i]:
        counts[i][word] += 1

matrix = np.zeros((n, len(words)))
for i in range(n):
    for word in counts[i]:
        matrix[i][words[word]] = counts[i][word]

distances = [0] * n
for i in range(n):
    distances[i] = distance.cosine(matrix[0], matrix[i])

min1, min2 = 1, 1
for i in range(1, n):
    if distances[i] < distances[min1]:
        min2 = min1
        min1 = i
    elif distances[i] < distances[min2]:
        min2 = i

answer = open("submission-1.txt", 'w')
answer.write(str(min1) + ' ' + str(min2))
answer.close()
