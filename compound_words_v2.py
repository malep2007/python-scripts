dict_list = ["water","big","apple","watch","banana","york","amsterdam","orange","macintosh","bottle","book"]
input_list = ["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle", "booking"]

dict_set = set(dict_list)
input_set = set(input_list)
compound_words = set([])


for word in dict_set:
    for input_word in input_set:
        if word in input_word and input_word.strip(word) in dict_list:
            compound_words.add(input_word)

print(compound_words)