### When the first conversion fails, it just drops into the except: clause
### and the program continues

astr = 'Hello Bob'
try:
    istr = int(astr) # Fails
except:
    istr = -1 # Prints

print('First', istr)

### When the second conversion succeeds, it just skips the except: clause
### and the program continues

astr = '126'
try:
    istr = int(astr) # Succeeds and prints
except:
    istr = -1

print('Second', istr)