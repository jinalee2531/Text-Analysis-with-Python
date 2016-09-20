'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : Dec. 12, 2015

Capstone Project Activity #5
Produce an listing of tokens / concepts along with their frequency 
and output them to the monitor in frequency ascending order. 

You must you an additional external library of your choosing to complete this activity.
You need to provide comments in your program. You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA5_LASTNAME_FIRSTNAME.py] and your external text files through Blackboard.  You may resubmit as many times as you like up to, the due date/time.  All work must be submitted via Blackboard.

'''


import nltk
from nltk.util import ngrams
# used to sort bag of words by frequency
import operator

def main():
    
    # read a text file: CAPSTONEA3_LEE_JINA_FILE1.txt
    filename='CAPSTONEA3_LEE_JINA_FILE1.txt'
    with open(filename,'r') as f:
        text=f.read()


    #referred to:  http://www.nltk.org/book/ch03.html        
    tokens = text.split()    
    tokens_nltk=nltk.Text(tokens)
    #print(tokens_nltk.collocations()) 
    
    
    #tokenize = nltk.word_tokenize(text)
    # bw: container for processed tokens, bag of words
    bw=[]
    
    # create Unigram list and put in a list 'a'
    unigrams = ngrams(tokens,1)
    for grams in unigrams:
        #print(grams)
        bw.append(grams)
    
    # create Bigram list and put in a list 'a'
    bigrams = ngrams(tokens,2)
    for grams in bigrams:
        #print(grams)
        bw.append(grams)
    
    # create Trigram list and put in a list 'a'
    trigrams = ngrams(tokens,3)
    for grams in trigrams:
        #print(grams)
        bw.append(grams)
    
    #freq : counting the number of occurrence of each word in bag of words, bw
    freq={}
    for key in bw:
        if key in freq.keys():
            #print('key in freq:::', freq.keys()) 
            freq[key]+=1
        else: freq[key]=1
    print('###########')
    
    '''
    # printing out freq
    for key, value in freq.items():
        print(key, value)
    '''
    
    # sort the freq dictionary by value in ascending order, using 'operator' library
    # referred to  - http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    
    # itemgetter(1): ordered by values, itemgetter(0): ordered by keys
    sorted_freq = sorted(freq.items(), key = operator.itemgetter(1))
    
    # print out sorted_freq dictionary
    for key, value in sorted_freq:
        print(key, value)
    
 
    
main()
    