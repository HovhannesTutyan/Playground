import re
import pandas as pd

pattern = '022515'
print('Match') if re.fullmatch(pattern, '022515') else print('No match')
print('Valid') if re.fullmatch(r'\d{6}', pattern) else print('Invalid') # r - raw string, \d{6} - 6 digits, \d{3,6} - 3 to 6 digits,  \D not digit, \s whitespace, \S not whitespace, \w word, \W not word
print('Valid') if re.fullmatch('[A-Z][a-z]*', 'Wally') else print('Invalid') # starts with uppercase and than lowercase, with *quantifier 0 or more for lowercase, + at least one lowercase
print('Valid') if re.fullmatch('[^a-z]*', 'WALLY') else print('Invalid') # any char that is not uppercase
print(re.split(r',\s', '1,2, 3,4,   5, 6, 7,8,9')) # ['1,2', '3,4', '  5', '6', '7,8,9']

result = re.search('Python', 'Python is fun') # flags=re.IGNORECASE for case-insensitive search
print(result.group()) if result else print('not found') # Python

contact = 'Wally White, Home: 555-555-2134, Work: 555-555-3546, Other: 34-52-2455'
filtered = re.findall(r'\d{3}-\d{3}-\d{4}', contact)
print(filtered) # ['555-555-2134', '555-555-3546']
for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group()) # 555-555-2134 555-555-3546


zips = pd.Series({'Boston':'02215', 'Miami':'3310'})
print(zips.str.match(r'\d{5}')) # check if zip code is 5 digits
# Boston     True
# Miami     False
# dtype: bool

cities = pd.Series(['Boston, M 02215', 'Miami, FL 33101'])
print(cities)
# 0    Boston, M 02215
# 1     Miami, FL 33101
# dtype: object
print(cities.str.contains(r' [A-Z]{2}'))
# 0    False
# 1     True
# dtype: bool

contacts = [['Mike Green', 'demo1@deitel.com', '5555555556'],
            ['Sue Brown', 'demo2@deitel.com', '1123445678']]
contactsdf = pd.DataFrame(contacts, columns=['Name', 'Email', 'Phone'])
print(contactsdf)
#          Name             Email      Phone
# 0  Mike Green  demo1@deitel.com  555555555
# 1   Sue Brown  demo2@deitel.com  112344567
def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value
formatted_phone = contactsdf['Phone'].map(get_formatted_phone)
print(formatted_phone)
# 0    555-555-5556
# 1    112-344-5678
contactsdf['Phone'] = formatted_phone
print(contactsdf)
#          Name             Email         Phone
# 0  Mike Green  demo1@deitel.com  555-555-5556
# 1   Sue Brown  demo2@deitel.com  112-344-5678