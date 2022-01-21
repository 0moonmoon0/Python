# find() finds the first occurence of the substring index

fruit = 'banana'
pos = fruit.find('na')
print(pos)  # Prints 2

aa = fruit.find('z')
print(aa) # Prints -1

spe = fruit.find('na', 3) # Starts at index 3
print(spe) # Prints 4

### replace() function searches for words and replaces them

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr) # Prints Jane instead of Bob

### strip() removes whitespace at the beginning and/or the end

greet = '    Hello Bob      '
greet.lstrip() # 'Hello Bob      '
greet.rstrip() # '       Hello Bob'
greet.strip() # 'Hello Bob'

### startswith() method returns True if the string starts with the specified value
greet = 'Hello Bob'
greet.startswith('Hello') # True

