import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ') # http://py4e-data.dr-chuck.net/known_by_Tala.html
count = int(input('Enter count: '))
position = int(input('Enter position: '))
print('Retrieving:', url)

for i in range(count):
    
    html = urllib.request.urlopen(url).read() 
    soup = BeautifulSoup(html, 'html.parser') 

    tags = soup('a') 
    for tag in tags[:position]:
        link = tag.get('href', None)
    print('Retrieving:', link)
    url = link
    
