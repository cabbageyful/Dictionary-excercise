# put your code here.
file_data = open('test.txt')

word_count = {}

for line in file_data:
    line = line.rstrip()
    line = line.split(' ')

    for word in line:
        word_count[word] = word_count.get(word, 0) + 1
        print word, word_count[word]
