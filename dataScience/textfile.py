import os
import json
import pandas as pd

# ============== Write ===============
# with open('accounts.txt', mode='w') as accounts:
#     accounts.write('100 Jones 24.98\n')
#     accounts.write('200 Doe   345.67\n')
#     accounts.write('300 White 0.00\n')
#     accounts.write('400 Stone -42.16\n')
#     accounts.write('500 Rich  244.62\n')

# ============== Read ===============
# with open('accounts.txt', mode='r') as accounts:
#     print(f'{"Account":<10} {"Name":<10} {"Balance":>10}')
#     for record in accounts:
#         account, name, balance = record.split()
#         print(f'{account:<10}{name:<10}{balance:>10}')

# ============== Update ===============
# accounts = open('accounts.txt', 'r')
# temp_file = open('temp.txt', 'w')
# with accounts, temp_file:
#     for record in accounts:
#         account, name, balance = record.split()
#         if account != '300':
#             temp_file.write(record)
#         else:
#             new_record = ' '.join([account, 'Williams123', balance])
#             temp_file.write(new_record + '\n')
# os.remove('accounts.txt')
# os.rename('temp.txt', 'accounts.txt')


# ============== JSON serializing ===============
# accounts_dict = {'accounts': [
#     {'account': 100, 'name': 'Jones', 'balance': 24.98},
#     {'account': 200, 'name': 'Doe', 'balance': 345.67}]}
# with open('accounts.json', 'w') as accounts:
#     json.dump(accounts_dict, accounts)

# ============== JSON deserializing ===============
# with open ('accounts.json', 'r') as accounts:
#     accounts_json = json.load(accounts)
#     print(accounts_json['accounts'][0])
#     # {'account': 100, 'name': 'Jones', 'balance': 24.98}

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
print((titanic.survived == 'yes').describe())
# count      1309
# unique        2
# top       False
# freq        809
# Name: survived, dtype: object