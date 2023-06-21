import math
print("To verify whether this number is daffodilNumber or not")
number = int(input("type in the number: "))
firstNumber = 0
secondNumber = 0
lastNumber = 0
while number % 2 != 0:
    lastNumber = lastNumber + 1
    number = number-1

newNumber = number/10
while newNumber % 2 != 0:
    secondNumber = secondNumber + 1
    newNumber = newNumber-1

new2Number = newNumber/10
while new2Number % 2 != 0:
    firstNumber = firstNumber + 1
    new2Number = new2Number-1

f = math.pow(firstNumber, 3)
s = math.pow(secondNumber, 3)
t = math.pow(lastNumber, 3)

if f+s+t == number:
    print("This number is a daffodilNumber.")
else:
    print("This number is not a daffodilNumber.")






