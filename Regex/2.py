'''
Python has a large number of Regular Expression functions

findall: Returns a list containing all matches
search: Returns a Match object if there is a match anywhere in the string
split: Returns a list where the string has been split at each match
sub: Replaces one or many matches with a string
'''


import re

txt='My name is Aswathy'

x=re.findall('a',txt)

print(x)

y=re.split(' ',txt)

print(y)

z=re.sub('Aswathy','Amal',txt)

print(z)

#output
'''
['a', 'a']
['My', 'name', 'is', 'Aswathy']
My name is Amal
'''