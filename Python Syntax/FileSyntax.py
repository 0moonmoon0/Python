### Opening file using rstrip

fname = input('Enter the file name: ') # Prompt for file name
fhand = open(fname) 
count = 0

for line in fhand: # Loops by each line
    line = line.rstrip() # Strips the whitespace from the right-hand side
    if line.startswith('From:'): # If first string starts with 'From:', count the line
        count = count + 1
print('There were', count, 'subject lines in', fname)  # There were 2929 subject lines in sample.txt

### Opening file using split

fhand = open('sample.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): # If line doesn't start with 'From', restart the loop
        continue
    words = line.split() # Split each word (whitespace) into a collection inside a list
    print(words[2]) 
    
