'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : Dec. 12, 2015

Capstone Project Activity 1


1.) Web scrape the following web site:  pick an alert from:  www.us-cert.gov/ncas/alerts/TA15-213A
I suggest using the requests external library to do this web scraping.

2.) Then, print the results to the monitor in a readable format,
- as if you wrote the web-site source code yourself (so it's readable, pretty).

'''

# used for scraping contents from web-page
import requests
# used to edit html documents in readable format
from bs4 import BeautifulSoup

# set the url to scrape 
url = r'https://www.us-cert.gov/ncas/alerts/TA15-213A'

# gets a response from the web page 
r = requests.get(url)

# extracting contents from the response
content = r.content.decode('utf-8')

# creating a BeautifulSOup object to parse the content
soup = BeautifulSoup(content, 'html.parser')

# arranging content in readable format, text type.
a=soup.prettify()#.encode('utf-8')


# to have only content we are interested, set a range of contents and subset it from the entire document.
## range is set as between <div class="content clearfix"> and <div class="clearfix">
start = r'<h1 id="page-title">'
end = r'<a id="revisions">'

#subsetting the content
a  = a[a.index(start):a.index(end)+len(end)]

# save the subsetted content as text file.
filename='ac1.txt'
with open(filename,'w', encoding='utf-8') as f:
    f.write(a)
    print(filename, 'is created.')

