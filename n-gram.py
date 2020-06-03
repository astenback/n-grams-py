#!/usr/bin/env python3

import nltk
import select
import sys
from collections import Counter, OrderedDict
from nltk import ngrams

'''
Generate ngrams
'''


def myNgrams(text, num, top):

    print("Processing text for top", top, "Ngrams of", num)
    # Tokenize input, convert to lowercase
    tokens = nltk.word_tokenize(text)
    for token in tokens:
        if len(token) >= 1:
            token = token.lower()

    # Remove non-alphanumeric characters (puncuation)
    tokens = [word for word in tokens if word.isalpha()]

    # Create ordered dictionary of ngrams
    myNgrams = ngrams(tokens, num)
    myList = (Counter(myNgrams))
    myOrderedDictOfNgrams = OrderedDict(myList.most_common(top))

    return myOrderedDictOfNgrams


'''
Execute main
'''
if __name__ == "__main__":

    # Sets the N in Ngram (bigram, trigram, etc)
    num = 3
    top = 5

    # Check stdin, if data is present process it, else check command line args
    if select.select([sys.stdin, ], [], [], 0.0)[0]:

        print("Stdin has data, processing it")

        text = ""
        for line in sys.stdin:
            text += line

        myOrderedDictOfNgrams = myNgrams(text, num, top)


    else:
        print("No data on std in, checking command line args")

        if len(sys.argv) <= 1:
            print("Usage: n-gram.py <text_file1> <text_file2> ...")

        else:

            print("Processing data from command line args")

            for i in sys.argv[1:]:
                # Open file, read and store text

                print("Reading " + i)
                f = open(i, "r")
                text = f.read()

                # Process Ngrams
                myOrderedDictOfNgrams = myNgrams(text, num, top)

                # Print key, values of the ordered dictiony returnd from myNgrams
                j = 1
                for key, value in myOrderedDictOfNgrams.items():
                    print("Top", j, "NGram of", num, "in", i, "is", key, 'with a count of', value)
                    j += 1

                # Close file
                f.close()


