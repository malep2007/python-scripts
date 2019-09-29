# dict_list = ["water","big","apple","watch","banana","york","amsterdam","orange","macintosh","bottle","book"]
# input_list = ["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle"]

# # def find_compound_words(some_input_list):
# #     compound_words = []
# #     for dict_word in dict_list:
# #         for input_word in input_list:
# #             if dict_word in input_word and input_word.strip(dict_word) != '' and input_word not in compound_words:
# #                 compound_words.append(input_word)


# #     return compound_words

dictionary = ["water","big","apple","watch","banana","york","amsterdam","orange","macintosh","bottle","book"]
def compound(word):
  compound = []
  for w in word:
    contained = []
    for sample in dictionary:
      if sample in w:
        contained.append(sample)
        if len(contained) >= 2:
          compound.append(w)
      
  return compound


dict_list = ["water","big","apple","watch","banana","york","amsterdam","orange","macintosh","bottle","book"]
input_list = ["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle", "booking"]

def find_compound_words(some_input_list):
    compound_words = []
    for dict_word in dict_list:
        for input_word in some_input_list:
            if (input_word.startswith(dict_word) or input_word.endswith(dict_word) ) and dict_word in input_word:
                compound_words.append(input_word)
    return compound_words

print(find_compound_words(["booking", "applewatch", "bigbook"]))

# print (find_compound_words(["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle", "booking"]))
# # print (compound(["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle", "booking"]))
