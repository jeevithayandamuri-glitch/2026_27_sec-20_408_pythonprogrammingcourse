#4A_Word_Frequency_Dictionary
sentence = "to be or not to be"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print("Frequency:", freq)