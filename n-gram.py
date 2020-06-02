#!/usr/bin/env python3

import sys
import select
import nltk
from nltk import ngrams
from nltk import trigrams
from collections import Counter

def my_ngrams_from_file():

    f = open(i, "r")

    tokens = nltk.word_tokenize(f.read())
    for token in tokens:
        if len(token) >= 1:
            token = token.lower()


    trigrams = ngrams(tokens,3)
    print(Counter(trigrams))

    f.close()

def my_ngrams_from_stdin(text):

    tokens = nltk.word_tokenize(text)
    for token in tokens:
        if len(token) >= 1:
            token = token.lower()

    trigrams = ngrams(tokens,3)
    print(Counter(trigrams))


if select.select([sys.stdin,],[],[],0.0)[0]:

    print("Have data! Printing it")

    text = ""
    for line in sys.stdin:
        text += line

    my_ngrams_from_stdin(text)

else:
    print("No data! Checking command line args")

    if len(sys.argv) <= 1:
        print("Usage: n-gram.py <text_file1> <text_file2> ...")
    else:
        print("Reading command line args")
        for i in sys.argv[1:]:
            my_ngrams_from_file()

