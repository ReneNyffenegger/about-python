from getpass import getpass

username = input  ('Username: ')
password = getpass('Password: ')

if username == 'Rene' and password == 'secretGarden':
   print('Bingo')
else:
   print('Wrong username or password')
