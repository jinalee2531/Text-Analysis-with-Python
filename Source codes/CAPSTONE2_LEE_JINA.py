'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : Dec. 12, 2015

Capstone Project Activity 2

1.) Cleanup your unstructured text by removing all web source code.
    I suggest using BeautifulSoup get_text() to do this, but it will also involve some manual coding on your part.
    
2.) Output the results to an external text file:  CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt

You need to provide comments in your program.
You should have a comment block at the start of your code that identifies yourself, original creation date, last modification date, and gives a description of the program. You will need to provide comments for each procedure and variable. Comments will be a part of each activity grade.

Submit your source code [filename = CAPSTONEA2_LASTNAME_FIRSTNAME.py] 
and  external file [filename = CAPSTONEA2_LASTNAME_FIRSTNAME_FILE1.txt]
 through Blackboard.  You may resubmit as many times as you like up to, the due date/time.  All work must be submitted via Blackboard.
Please keep in mind that you cannot skip activities.  You work at your own pace.


'''

import requests
from bs4 import BeautifulSoup



def main():
    
    #read a content saved in activity 1
    with open('ac1.txt', 'r') as f:
        content = f.read() 
    
    # generating BeautifulSoup object to parse HTML file
    soup = BeautifulSoup(content, 'html.parser')
    
    # getting only texts from content
    text_raw = soup.get_text()
    
    # save texts as text file
    with open('text_raw.txt','w') as f:
        f.write(text_raw)
       
    # 1. removing web source codes, which are appearing with strings
    '''
        1. between <!--//--> and //--><!]]>
        2. between <!--/*--> and /*--><!]]>*/
        3. between jQuery and });
    '''
    
    ## creating a dictionary contains pairs words indicating of starting and end of source code. 
    removeDic={}
    removeDic[r'<!--//-->'] = r'//--><!]]>'
    removeDic[r'<!--/*-->'] = r'/*--><!]]>*/'
    removeDic['jQuery'] = r'});'
    
    ## removing source code
    text=removeThisRange(text_raw,removeDic)
    print('###### removed source codes ######')
    
    
    # 2. modifying proper nouns and terms
    # setting a dictionary of words that need to be modified to avoid parsing these words in a wrong way while creating a bag of words 
    modDic={}
    modDic['U.S.'] = 'United States'
    modDic['(US-CERT)'] = ' '
    modDic['US-CERT'] = 'us-cert'
    modDic['United State Computer Emergency Readiness Team'] = 'us-cert'
    modDic['CVE'] = 'cve'
    modDic['VP'] = 'vp'
    modDic['TAA'] = 'taa'
    modDic['ZIP'] = 'zip'
    modDic['IP'] = 'ip'
    modDic['DNS'] = 'dns'
    modDic['ExMerge'] = 'Exmerge'
    modDic['IDS'] = 'ids'
    modDic['AV'] = 'av'
    modDic['VLAN'] = 'vlan'
    modDic['NCCIC'] = 'nccic'
    modDic['IT'] = 'info-technology'
    modDic['PIV'] = 'piv'
    modDic['YARA'] = 'yara'
    modDic['ICS-CERT'] = 'ics-cert'
    
    ## modifying words in modDic dictionary
    text=replaceText(text,modDic);print('###### replaced dictionary values ######')
    
    
    ### save text as txt file
    outputFile='CAPSTONEA2_LEE_JINA_FILE1.txt'
    with open(outputFile,'w') as f:
        f.write(text)
        print(outputFile,' has been created.')


# find index of each string representing begin and end of web-source code,
# then will remove all characters between start index and end index.
def removeThisRange(text,removeDic):
    # key: start string, value: end string
    for key, value in removeDic.items():
        while(text.find(key)!=-1):
            idx_start = text.index(key)
            idx_end = text.index(value)+len(value)
            # to debug the part to be removed
            #print('\n##############REMOVING: ',text[idx_start:idx_end])
            text = text[:idx_start-1]+'\n'+text[idx_end+1:]
    return text

# to substitute words with pre-set words 
def replaceText(text,modDic):
    for key, value in modDic.items():
        while(text.find(key)!=-1):
            text = text.replace(key, modDic[key])
    return text
            
        

main()