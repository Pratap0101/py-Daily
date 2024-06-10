# 10 - Jun - 2024
# pg - No  - 147 to 152
# In this chapter, you’ll start by writing a program to find text patterns


# Finding Patterns of Text Without Regular Expressions

def fnd_mob_num(text):

    if len(text) != 12:
        return False
        
    
    for i in range(0, 3):
        
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False
    
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False
    
    for i in range(8,12):

        if not text[i].isdecimal():
            return False

    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if fnd_mob_num(chunk):
        ''
        # print('Phone number found: ' + chunk)
        
# print('Done')

# otp : -
# Phone number found: 415-555-1011
# Phone number found: 415-555-9999
# Done

# With Regular Expression
import re

fnd_ph_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

num = fnd_ph_num.search('Phone number found: 415-555-1011')

# print(num.group())


# group Regular Expression
fnd_ph_num = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

num = fnd_ph_num.search('Phone number found: 415-555-1011')

# print(num.group(1))
# print(num.group(2))