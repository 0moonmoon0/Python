import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter - ') # http://py4e-data.dr-chuck.net/comments_1466782.html
html = urllib.request.urlopen(url).read() # Read html file in one line
soup = BeautifulSoup(html, 'html.parser') # Formats html file 

# Retrive all of the anchor tags
tags = soup('a') # http://www.dr-chuck.com/page1.htm
for tag in tags:
    print(tag.get('href', None))



numList = soup.findAll("span", {"class":"comments"}) # <span class="comments">
numbers = []
for num in numList:
    numbers.append(num.get_text()) # Get text between <>___<>

numbers = list(map(int, numbers)) # Change all string into integer
print("Count", len(numbers))
print("Sum", sum(numbers))

### Useful Links
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=htk1019&logNo=220968562764