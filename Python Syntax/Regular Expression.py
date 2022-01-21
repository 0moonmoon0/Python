"""""
Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times 
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times 
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
"""""

import re # <--- IMPORT

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y) # ['From:']

a = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2009'
b = re.findall('\S+@\S+', a)
print(b) # ['stephan.marquard@uct.ac.za']

c = re.findall('^From (\S+@\S+)', a)
print(c) # ['stephan.marquard@uct.ac.za']

d = re.findall('@([^ ]*)', a)
print(d) # ['uct.ac.za']

### The basic outline of this problem is to read the file, look for integers using 
###  the re.findall(), looking for a regular expression of '[0-9]+' and then converting 
### the extracted strings to integers and summing up the integers.

numbers = []
info = open('regex_sum_1466780.txt', 'r')
for line in info:
    num = re.findall('[0-9]+', line)
    if len(num) > 0:
        numbers.extend(num)

intnum = list(map(int, numbers))
print(sum(intnum)) # 337163

