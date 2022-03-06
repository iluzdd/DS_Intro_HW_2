###############################
# Assignment 2
# Dvir David Iluz
# 311447668
###############################

# A. 

from operator import index


def reverse(sentence, reverse_word):
    try:
        if not isinstance(sentence,str) or not isinstance(reverse_word,str):
            raise TypeError
        split_to_words = sentence.split(" ")
        for word in split_to_words:
            if word == reverse_word:
                sentence = sentence.replace(reverse_word, reverse_word[::-1],1)
                return sentence
        return "no match word found"
    except TypeError:
        return "Invalid input detected"

# B. 

def compute_equation(equation):
    try:
        if not isinstance(equation,str):
            raise TypeError
        return eval(equation)
    except TypeError:
        return "input can only be a string"