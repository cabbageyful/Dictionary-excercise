# put your code here.

def counting_words(file_data):
    """Finds total count of each word in file.

    Iterates over file to determine the word count for each
    word in the file using a dictionary. 
    """

    file_data = open(file_data)

    word_count = {}

    my_list = []

    for line in file_data:
        line = line.rstrip()
        line = line.split(' ')
        my_list.extend(line)

    
    for word in my_list:
        word_count[word] = word_count.get(word, 0) + 1
        # print word, word_count[word]
    return word_count

print counting_words('test.txt')