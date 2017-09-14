# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:09:12 2017

@author: Administrator
"""

def break_words(stuff):
    """" this function will break up words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ sorts the words """
    return sorted(words)

def print_first_word(words):
    """print the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """print the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and teturn the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """print the first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    