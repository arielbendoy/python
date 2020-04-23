Pets = ['Acey', 'Theodore', 'Fat-tail']

print('Enter a pet name: ')
name = input()
if name not in Pets:
    print('Pet name not in list.')

else:
    print(name + ' is in list.')