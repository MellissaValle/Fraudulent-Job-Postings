import numpy as np
import pandas as pd
import string

#remove weird numbers
def remove_number(text):
    numbers_to_remove = ['1', '2', '3', '4','5', '6', '7', '8', '9', '0', "\xa0" ]
    clean_text = text
    for num in numbers_to_remove:
        clean_text = clean_text.replace(num, ' ')
    
    return clean_text


def remove_punctuations(text):
    for punctuation in punctuations:
        text = text.replace(punctuation, ' ')
    return text