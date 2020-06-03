#!/usr/bin/env python3

import nltk
import select
import sys
from collections import Counter, OrderedDict
from nltk import ngrams
nltk.download('punkt')

'''
Function to generate ordered dictionary of n-grams. Ordered descending from most occurrences to least
'''


def myNgrams(text, num, top):
    # Tokenize input, convert to lowercase
    print("Processing text for top", top, "n-grams of", num)
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens]

    # Remove non-alphanumeric characters (puncuation)
    tokens = [word for word in tokens if word.isalpha()]

    # Create ordered dictionary of ngrams
    myNgrams = ngrams(tokens, num)
    myList = (Counter(myNgrams))
    myOrderedDictOfNgrams = OrderedDict(myList.most_common(top))

    return myOrderedDictOfNgrams

'''
Function to print n-grams
'''


def printMyOrderedListOfNgrams(myOrderedDictOfNgrams):
    # Print key, values of the ordered dictiony returnd from myNgrams
    j = 1
    for key, value in myOrderedDictOfNgrams.items():
        print("Top", j, "n-gram of", num, "is", key, 'with', value, "occurrences")
        j += 1

'''
Execute main
'''
if __name__ == "__main__":

    # Sets the N in Ngram (bigram, trigram, etc) and top number (Top 10, Top 25, etc)
    num = 3
    top = 100

    # Check stdin, if data is present process it, else check command line args
    if select.select([sys.stdin, ], [], [], 0.0)[0]:

        print("Stdin has data, processing it")

        text = ""
        for line in sys.stdin:
            text += line

        myOrderedDictOfNgrams = myNgrams(text, num, top)
        printMyOrderedListOfNgrams(myOrderedDictOfNgrams)


    else:
        print("No data on std in, checking command line args")

        if len(sys.argv) <= 1:
            print("")
            print("USAGE:")
            print("")
            print("./n-grams.py <text_file1> <text_file2> ...")
            print("")
            print("or")
            print("")
            print("cat MobyDick.txt | ./n-grams.py")
            print("echo \"Hello, HeLLo, HELLO.\" | n-grams.py")
            print("")

        else:

            print("Processing data from command line args")

            for i in sys.argv[1:]:
                # Open file, read and store text

                print("Reading " + i)
                f = open(i, "r")
                text = f.read()

                # Process n-grams
                myOrderedDictOfNgrams = myNgrams(text, num, top)
                printMyOrderedListOfNgrams(myOrderedDictOfNgrams)

                # Close file
                f.close()