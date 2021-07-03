#working with regular expressions using re library

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | (  )

coreyms.com

321-555-4321
123.555.1234
Mr.Schafer
Mr. Smith
Ms Davis
Mrs. Robinson
'''

sentence = "Start a sentence and then bring it to an end"

print(r'\tTab') #this is a raw string as r is written before quotation

pattern = re.compile(r'\.') #case sensitive

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print(text_to_search[1:4])


