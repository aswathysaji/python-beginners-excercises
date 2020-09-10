
import re
txt = "My name is Aswathy"
x = re.search(" is ", txt)
print(x.span()) #.span() returns a tuple containing the start-, and end positions of the match.
print(x.string) #.string returns the string passed into the function
print(x.group()) #.group() returns the part of the string where there was a match