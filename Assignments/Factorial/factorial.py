def factorial(numArg):
    if numArg < 2:
        if numArg == 0 or numArg == 1:
            return 1
        else:
            return "Cannot be negative number."
    else:
        numArg *= factorial(numArg-1)

    return numArg
    
print(factorial(3)) # 6
print(factorial(10)) # 3628800
print(factorial(6)) # 720