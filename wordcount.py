#def ine funcion that takes in text file name as argument
#open and store text file data into a file handle object
#use a for loop to create a list of words (use rstrip and split methods)
#use a for loop to create a dictionary based on list elemnts and count them with .get method
#print keys and values


def word_counter(filename):
    text_file = open(filename)

    dictionary_of_words = {}

    for line in text_file:
        line = line.rstrip() # why is this different than just line.rstrip() ?
        words = line.split(' ')

        for word in words:
            dictionary_of_words[word] = dictionary_of_words.get(word, 0) + 1

    for key in dictionary_of_words:
        # print(key, dictionary_of_words[key])  
        print(f'{key} {dictionary_of_words[key]}')
        # print("{} {}".format(key, dictionary_of_words[key]))

    # return dictionary_of_words

    # return words

# print(word_counter('test.txt'))
word_counter('test.txt')
# word_counter("twain.txt")