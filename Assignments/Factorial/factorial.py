def factorial(numArg):
    if numArg < 2:
        if numArg == 1 or numArg == 0:
            return 1
        else:
            return "Error. Must be a positive number."
    else:
        numArg *= factorial(numArg-1)
    return numArg

print(factorial(6)) # 720
print(factorial(10)) # 3628800
print(factorial(3)) # 6