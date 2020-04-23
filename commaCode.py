spam = ['apples', 'bananas', 'tofu', 'cats']
cheese = ['john doe', 'jane doe', 'josh doe', 'james doe']

def getValues(list):
    returnString = ''

    lastString = list[len(list)-1]
    lengthString = int(len(list) - 1)
    print(lastString)
    #print(lengthString)
    newList = list[0:lengthString]
    #print(newList)
    for words in newList:
        returnString += words + ' ,'
    #print(returnString)
    #print(returnString + ' and ' + lastString)

getValues(spam)
getValues(cheese)