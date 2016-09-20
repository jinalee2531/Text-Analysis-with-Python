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
# to get a list of punctuations
import string
# to get a list of stopwords
from nltk.corpus import stopwords
# to use for Porter stemming
from nltk.stem.porter import *
# to use for Snowball stemming
from nltk.stem.snowball import SnowballStemmer
# for general text processing
import nltk
# for generating ngrams
from nltk.util import ngrams
# for editing texts
import re

def main():
    
    ### 1) print out 'CAPSTONEA2_LEE_JINA_FILE1.txt' file
    filename='CAPSTONEA2_LEE_JINA_FILE1.txt'
    with open(filename,'r') as f:
        text=f.read()
    print(text)

    # creating a nltk document object to generate ngram from the original document
    tokens = text.split()
    tokens_nltk=nltk.Text(tokens);
    
    
    ###2) REMOVING NOISE 
    
    ## 2)-1 removing punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    myPunctuation = string.punctuation # ; print('before: ',myPunctuation)
    # exclude '-' from punctuation list
    myPunctuation=myPunctuation.replace('-','') #; print('after: ',myPunctuation)
    # removing punctuation from the document, stored as list of tokens
    nopunct = [w for w in text if w not in myPunctuation ] #print(string.punctuation)
    # generate a line with tokens
    withoutPunctuation = ''.join(nopunct) ;print(withoutPunctuation)
  
    
    ## 2)-2 split by upper case for some words are not spaced in the document, ex) 'appleBanana' -> 'apple Banana'
    # a list to restore processed tokens
    new=[]
    for token in withoutPunctuation.split():
        # split a token if it contains upper case between second character and last character
        if(any(chr.isupper()==True for chr in token[1:])):
            splited= re.findall('[A-Z][a-z]*', token)
            #print(splited)
            for s in splited:
                new.append(s)
        else : new.append(token)
    
    withoutPunctuation = new
        
    ## 2)-3 Change entire texts to lower case
    a = [word.lower() for word in withoutPunctuation] 
    withoutPunctuation = a     
    
    ## 2)-4 Remove stopwords
    # getting a list of stopwords
    my_stops = stopwords.words('english') #;  print(my_stops)
    # add additional stopwords
    my_stops.append('eg')
    my_stops.append('would')
    
    # getting rid of stopwords
    normalized = [w.lower() for w in withoutPunctuation if w.lower() not in my_stops]
    
    # joining all tokens in a line 
    norm_text = ' '.join(normalized)
   
    
    ## 2)-5 Stemming; tried two types of stemmer, Porter stemmer and Snowball stemmer
    
    # getting a Stemmer object
    stemmer_porter = PorterStemmer()
    stemmer_sb = SnowballStemmer("english")
    
    # specify a Stemmer to use
    stemmer=stemmer_sb
    
    # Processing stemming
    stemmed = [stemmer.stem(token) for token in normalized]
    
    # joining entire tokens of stemmed list in a line
    stemmed_line = ' '.join(stemmed);     #print(stemmed_line)
    
    # save the line in text file
    filename = 'CAPSTONEA3_LEE_JINA_FILE1.txt'
    with open(filename,'w') as f:
        f.write(stemmed_line)
    print ('\n',filename,'is created.')


main()


