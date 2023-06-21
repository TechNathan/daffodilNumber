import math
print("This is going to verify whether your number is daffodilNumber or not")
number = int(input("Type in your number: "))
thirdNumber = number % 10
secondNumber = number // 10 % 10
firstNumber = number // 100
if math.pow(thirdNumber, 3)+math.pow(secondNumber, 3)+math.pow(firstNumber, 3)==number:
    print("This number is a daffodilNumber.")
else:
    print("This number is not a daffodilNumber.")






