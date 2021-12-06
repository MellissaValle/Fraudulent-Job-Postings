import numpy as np
import pandas as pd
import string

# Create our list of punctuation marks
punctuations = string.punctuation

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

#removes weird symbols
def remove_symbols(text):
    symbols_to_remove = ["\xa0", " \n ", '\n', " <div> ", "<li>", '<br>', '</ul>' , '<b>'," d "," y "," q ","</li>", '<ul>','</b>', '</div>','<div', " p ", ' jz ', ' iu ','class=' ,'jz'\
                         'jobDescriptionText' , 'jobdescriptiontext', 'class','jobsearch']
                       
    clean_text = text
    for sym in symbols_to_remove:
        clean_text = clean_text.replace(sym, ' ')
    
    return clean_text

# Taken from: https://www.dataquest.io/blog/tutorial-text-classification-in-python-using-spacy/ 
# Custom transformer 
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        # Cleaning Text
        return [clean_text(text) for text in X]
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def get_params(self, deep=True):
        return {}
