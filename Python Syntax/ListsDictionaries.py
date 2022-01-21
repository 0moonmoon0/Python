### List dir terminology

from re import L


lst = list()
lst.append('3') # Adds 23 in a list. Also appends nested lists
lst.extend('132') # Adds '1', '3', '2' in a list. Useful for adding single lists
lst.sort(reverse = True) # Sorts list in reverse order
print(lst)

### Dictionary dir terminology

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd) # {'course': 182, 'age': 21}
ddd['age'] = ddd['age'] + 1 # age becomes 21 + 1 = 22

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # If there is no name in the dictionary, 
print(counts)                              # create a new one. Count every names using + 1

### Dictionary, File example

counts = dict()
line = input('Ener a line of text: ') # Calculates the number of words in given line
words = line.split()

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

### Dictionary properties

jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj)) # ['chuck', 'fred', 'jan']
print(jjj.keys()) # dict_keys(['chuck', 'fred', 'jan'])
print(jjj.values()) # dict_values([1, 42, 100])
print(jjj.items()) # dict_items([('chuck', 1), ('fred', 42), ('jan', 100)])

for aaa, bbb in jjj.items():
    print(aaa, bbb) # Prints out both keys and values

for k, v in sorted(jjj.items(), reverse = True): # Sorts keys in reverse
    print(v, k) # Print in value - key order
    
print( sorted( [ (v,k) for k,v in jjj.items() ] ) ) # list comprehension in tuples