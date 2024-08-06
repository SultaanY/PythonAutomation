# checks the strength of your passwords using regex
import re

password = input('Please enter a password that is between 8 and 15 characters, 1 special character and no spaces: ') 
passRegex = re.compile(r'.{8,15}')        #length between 8 and 15 characters
charRegex = re.compile(r'[^A-Za-z0-9]')   #checks for a special character
upcaseRegex= re.compile(r'[A-Z]')         #upper case check
lowcaseRegex = re.compile(r'[a-z]')       #lower case check
numRegex= re.compile(r'[0-9]')            #number case check
noSpaceRegex = re.compile(r'^\S+$')       #no space regex
# examplepass= 'QWERTYq123!'



if (passRegex.search(password) and 
    charRegex.search(password) and 
    upcaseRegex.search(password) and 
    lowcaseRegex.search(password) and 
    numRegex.search(password) and
    noSpaceRegex.search(password) ):
    print('Strong password')
else:
    print('Weak password, please enter a password longer than 8 characters, 1 special character, 1 digit and both lower and uppercase')