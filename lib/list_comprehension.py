#!/usr/bin/env python3

def return_evens(num_list):
    pass

def make_exclamation(sentence_list):
    pass
# lib/list_comprehension.py

def return_evens(sequence):
 
    return [n for n in sequence if n % 2 == 0]


def make_exclamation(sentences):
    if not sentences:
        return []
    # Ensure the input is a list of strings
    if not all(isinstance(s, str) for s in sentences):
        raise ValueError("All elements in the input must be strings.")
    # Add an exclamation mark to each sentence
    return [s + "!" for s in sentences]
 # Ensure the string is not empty