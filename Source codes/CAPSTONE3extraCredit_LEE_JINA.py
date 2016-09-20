'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    :  Dec. 12, 2015

Capstone Project Activity #3
1.) Print out CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt,
 and manually identify the noise and normalization you have to complete.
  
Prior to completing step #1, you can use the NLTK library to create a small program 
to make a list of ngrams of size 3 that may help you find compound concepts
 (which you then print to a temporary file).
If you create this small program, please attach it to your submission as CAPSTONEA3extraCredit_LASTNAME_FIRSTNAME.py for extra credit.  If you choose not to do this step, you have to identify the compound concepts manually in step #1.

2.) Replace all noise, punctuation and whitespace, and perform appropriate substitutions
 for stemming, creating compound concepts, and normalization.
You can use the NLTK library to help with this, but it will also involve some manual coding 
on your part.

3.) Output the new results to a second external text file:  CAPSTONEA3_LASTNAME_FIRSTNAME_FILE1.txt
You need to provide comments in your program. You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA3_LASTNAME_FIRSTNAME.py] and external file [filename = CAPSTONEA3_LASTNAME_FIRSTNAME_FILE1.txt] through Blackboard.  Also submit your source code for the extra credit if you decided to do it [filename = CAPSTONEA3extraCredit_LASTNAME_FIRSTNAME.py]
'''
# to parse html file
from bs4 import BeautifulSoup

# for general text processing
import nltk
# for generating ngrams
from nltk.util import ngrams


def main():
    
    ### 1) print out 'CAPSTONEA2_LEE_JINA_FILE1.txt' file
    filename='CAPSTONEA2_LEE_JINA_FILE1.txt'
    with open(filename,'r') as f:
        text=f.read()
    print(text)

    # creating a nltk document object to generate ngram from the original document
    tokens = text.split()
    tokens_nltk=nltk.Text(tokens);
    
    # generating trigrams 
    trigrams = ngrams(tokens,3)
    for grams in trigrams:
        print(grams)
    
    
  
main()


