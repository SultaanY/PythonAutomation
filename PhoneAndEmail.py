#! python 3

#Finds phone numbers and email addresses on the clipboard

import pyperclip, re

#for US numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\)) # area code
    (\s|-|\.)?         # seperator
    (\d{3})            # first 3 digits
    (\s|-|\.)?         # seperator
    (\d{4})            # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
    )''', re.VERBOSE)

ukRegex = re.compile(r'\d{11}|\+44\d{10}')

emailRegex = re.compile(r'''(
    (\w+|\.)              #username
    @             # at symbol
    (\w+|\.)             # domain name
    (\.)              # seperator
    (\w+|\.)+   # final part
     )''', re.VERBOSE)

text= str(pyperclip.paste())
matches = []
print(phoneRegex.findall(text))
for groups in phoneRegex.findall(text):
    # print(groups[0])
    phoneNum= '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' +groups[8]
    matches.append(phoneNum)

# print(emailRegex.findall(text))
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(ukRegex.findall(text))
for groups in ukRegex.findall(text):
    # print(type(groups))
    matches.append('UK: '+ groups)

# print(matches)

if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No relevant information found')
        