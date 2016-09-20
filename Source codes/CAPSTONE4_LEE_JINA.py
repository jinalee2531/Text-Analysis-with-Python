'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : Dec. 12, 2015

Capstone Project Activity #4
Produce an listing of tokens / concepts and output them to the monitor in ascending order.
You must you an additional external library of your choosing to complete this activity.

Submit your source code [filename = CAPSTONEA4_LASTNAME_FIRSTNAME.py]
and external text files through Blackboard.


'''


import nltk
from nltk.util import ngrams

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
    
    # getting a list of unique words    
    wv = list(set(bw)) #; print(len(bw),len(wv))
    
    # sort the wv list
    wv.sort()
    
    
    # printing out the sorted wv list
    print('###########')
    for w in wv:
        print (w)
        
    
    
    


    
main()