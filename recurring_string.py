# import types
# def repeated_character(some_string: str):
#     some_string_list = list(some_string)
#     none_repeated_char_list = []
#     count = 0
#     while True:
#         for char in some_string_list:
#             if char not in none_repeated_char_list:
#                 none_repeated_char_list.append(char)
#             else:
#                 return char
#                 break
#         return None


# import timeit

# def repeated_character(some_string: str):
#   some_string_list = {}
#   for char in some_string:
#     if char in some_string_list:
#       return char
#     some_string_list[char] = char
#   return None


import timeit

setup = '''
import random
import types

def repeated_character(some_string: str):
  some_string_list = {}
  for char in some_string:
    if char in some_string_list:
      return char
    some_string_list[char] = char
  return None



random.seed('slartibartfast')
s = [random.random() for i in range(100000)]

'''



setup2 = '''
import random

def repeated_character(some_string: str):
    some_string_list = list(some_string)
    none_repeated_char_list = []
    count = 0
    while True:
        for char in some_string_list:
            if char not in none_repeated_char_list:
                none_repeated_char_list.append(char)
            else:
                return char
                break
        return None

random.seed('slartibartfast')
s = [random.random() for i in range(1000)]

'''
print (min(timeit.Timer('a=s[:]; repeated_character(a)', setup=setup).repeat(7, 1000)))
print (max(timeit.Timer('a=s[:]; repeated_character(a)', setup=setup).repeat(7, 1000)))
#print (min(timeit.Timer('a=s[:]; repeated_character(a)', setup=setup2).repeat(7, 1000)))


