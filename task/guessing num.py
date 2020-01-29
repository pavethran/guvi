import random
def ran():
    n = random.randint(1, 99)
    return n
n = ran()   
guess = int(input("Enter an integer from 1 to 99: "))
print(n)
if(guess == n):
    print('u won')
else:
    print('ulost')
    