catNames = []
while True:
    print('Enter names of cat' +  str(len(catNames) + 1) + ' Or enter nothing to stop:')
    name = input()
    
    if name == '':
        print('Input Process Stopped')
        break
    catNames = catNames + [name]

print('The cat names are: ')
for name in catNames:
    print(''+ name)
