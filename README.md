# n-grams-py

Search text for n-grams and print top occurrences. Accepts text from file or
stdin. Punctuation is removed and text is processed case-insensitively, since
everthing is converted to lowercase. n and number of top occurrences to print 
are both configurable via variables num and top 

PREREQUISITES:

Python3, the Natural Language Toolkit and the Punkt Tokenizer Models are
prerequisites. NLTK must be installed as follows:

    $ pip3 install nltk

Punkt is downloaded using the nltk downloader within the script

USAGE:

    $ ./n-grams.py <text_file1> <text_file2> ...

or

    $ cat MobyDick.txt | ./n-grams.py
    $ cat OriginOfSpecies.txt | ./n-grams.py
    $ echo "Hello, HeLLo, HELLO." | ./n-grams.py

Sample Output:

    Stdin has data, processing it
    Processing text for top 100 n-grams of 3
    Top 1 n-gram of 3 is ('the', 'sperm', 'whale') with 111 occurrences
    Top 2 n-gram of 3 is ('of', 'the', 'whale') with 94 occurrences
    Top 3 n-gram of 3 is ('the', 'white', 'whale') with 84 occurrences
    Top 4 n-gram of 3 is ('one', 'of', 'the') with 64 occurrences
    Top 5 n-gram of 3 is ('out', 'of', 'the') with 58 occurrences
    ...

