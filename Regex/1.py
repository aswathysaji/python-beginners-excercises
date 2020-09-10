'''A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

Import the re module'''

import re

txt='My name is Aswathy'
x=re.search('^My.*Aswathy$',txt)
if x:
    print('Matching')
else:
    print('Not a match')

'''
"^" Starts with "^hello"
"$$" Ends with "world$"
"*" Zero or more occurrences "*"
'''

#output

'''
Matching
'''