import sys

def collatz(number):
        if number % 2 == 0 :
            answer = number // 2

        elif number % 2 == 1 :
            answer = number * 3 + 1
                
        while answer != 1:
            print(answer)
            number = answer
            return collatz(number)

        while answer == 1:
            print(answer)
            sys.exit()

try:
    number = int(input())
    collatz(number)
except ValueError:
    print('Input not valid')
    collatz(number)