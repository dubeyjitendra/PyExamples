# Regular Expression
# Findall
# Match
# Compile
# Sub
# Finditer
# Search
# Spilt

#Pleaase Refer this link
#https://docs.python.org/3/howto/regex.html

# Regular Expression Definition :
#A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, 
#using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world. The module re provides 
#full support for Perl-like regular expressions in Python.

#Instead of using above function we will read some metacharcters below are:
## Metacharcters
#? , . ,[] ,{} , + ,* , \d ,\D,\s ,\S, |, ^ , $, |w, \W,\w+ many more


# Regular Regression :

#1- Match
import re
'''sent="ssdd..de...sdfdrewrw 12123 43455"
pattern_match='ssdd'
matcher=re.match(pattern_match,sent)
print(matcher)
print('Match Start: {} , Match end: {} and match char : {} '
       .format(matcher.start(),matcher.end(),matcher.group()))'''

#2 Search
'''sent="ssdd..de...sdfdrewss 12123 43455 dr"
pattern_match='dr'
matcher=re.search(pattern_match,sent)
#print(matcher)
print('Match Start: {} , Match end: {} and match char : {} '
       .format(matcher.start(),matcher.end(),matcher.group()))'''

# Findall
'''sent="ssdd..de...sdfdrewss 12123 43455 dr"
pattern_match='dr'
matcher=re.findall(pattern_match,sent)
for matchervalue in matcher:
    print(matchervalue)'''

# Finditer
'''sent="ssdd..de...sdfdrewss 12123 43455 dr"
pattern_match='dr'
matcher=re.finditer(pattern_match,sent)
for matchervalue in matcher:
    print('Match Start: {} , Match end: {} and match char : {} '
          .format(matchervalue.start(), matchervalue.end(), 
          matchervalue.group()))'''

# Compile
'''sent="ssdd..de...sdfdrewrw 12123 43455"
pattern_match= re.compile('ss')
matcher=pattern_match.finditer(sent)
for matchervalue in matcher:
    print('Match Start: {} , Match end: {} and match char : {} '
          .format(matchervalue.start(), matchervalue.end(),matchervalue.group()))'''
# Sub
'''sent="ssdd..de...sdfdrewss 12123 43455 dr"
pattern_match='dr'
matcher=re.sub(pattern_match,'doctor',sent)
print(matcher)'''


# Spilt

'''sent="ssdd de sdfdrewss 12123 43455 dr"
matcher=re.split(' ',sent)
print(matcher)'''
#for item in matcher:
 #   print(item)
#s=" ".join(matcher)
#print(s)


# \d -> only digits
# \d+ -> digit with occurance
# \D -> except Digits
'''sent="ssdd de sdfdrewss 12123 43455 dr "
matcher=re.findall('\D+',sent)
print(matcher)'''

# \w -> all words(charaters and numbers)
# \w+ -> words with occurance
# \W ->  except charaters and numbers (special characters)
'''sent="ssdd de sdfdrewss 12123 43455 dr &"
matcher=re.findall('\W',sent)
print(matcher)'''

# . any characters
# [] Represent a character class
# {} number of occurrences
# ? Matches zero or one occurrence
sent="sssdd de sdfdrewss 12123 49455 dr &"
#matcher=re.findall('.',sent)
#print(matcher)
#matcher=re.findall('[0-5]{4}',sent)
#print(matcher)
#matcher=re.finditer('ss?',sent)
#print(matcher)
#for matchervalue in matcher:
    #print('Match Start: {} , Match end: {} and match char : {} '
          #.format(matchervalue.start(), matchervalue.end(),matchervalue.group()))


# ^
# $
# \s
'''matcher=re.findall('\s',sent)
print(matcher)
matcher=re.findall('[^\d]',sent)
print(len(matcher))'''
'''matcher=re.findall('[\d$]',sent)
print(len(matcher))'''

# Finding email
#ss='this is my email@gmail.com and jomesh@gmail.com'
#matcher=re.findall('\w+@\w+.\w+',ss)
#matcher=re.findall('\w+@\w+[.]\w+',ss)
#print(matcher)
# by taking input user end
'''usrinput=input('Enter your email address : ')
matcher=re.findall('\w+@\w+[.]\w+',usrinput)
if(len(matcher)> 0):
    print('matched')
else:
    print('Not Matched')'''

# IGNORECASE
'''sent='hi john,Hi John'
matcher=re.findall('hi',sent,re.IGNORECASE)
print(matcher)'''
# MULTILINE
'''sent='hi john,\n hi John\n hi'
matcher=re.findall('hi',sent,re.MULTILINE)
print(matcher)'''
