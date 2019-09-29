"""
Assume we have a list of words from the English dictionary, like: 
EnglishWords: 
[""water"",""big"",""apple"",""watch"",""banana"",""york"",""amsterdam"",""orange"",""macintosh"",""bottle"",""book""]

And another long list of string to process, write a function to identify ""compound words"" and return them:
input: [""paris"",""applewatch"",""ipod"",""amsterdam"",""bigbook"",""orange"",""waterbottle""]
output: [""applewatch"",""bigbook"",""waterbottle""]

"""

def compound_words(input_list):
    dictionary = tuple(['water', 'big', 'apple', 'watch', 'banana', 'york', 'amsterdam', 'orange', 'macintosh', 'bottle', 'book'])
    my_words = [word for word in input_list if word.endswith(dictionary)]
    return my_words

print(compound_words(['paris', 'applewatch', 'ipod', 'amsterdam', 'bigbook', 'orange', 'waterbottle']))