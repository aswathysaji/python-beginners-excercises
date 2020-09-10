'''String without vowels'''

str=input("Enter a string:")
new=''
for s in str:
    if s not in 'aeiou':
        new=new+s
print(new)

#outut

'''
Enter a string:aswathy saji
swthy sj
'''