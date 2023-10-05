def fibonacci(numArg):
    if numArg < 2:
        if numArg == 1 or numArg == 2:
            return 1
        elif numArg == 0:
            return 0
        else:
             return "Error. Must be a positive number."
    else:
        return (fibonacci(numArg-1) + fibonacci(numArg-2))

print(fibonacci(-1)) # ERROR.
print(fibonacci(0)) # 0
print(fibonacci(1)) # 1
print(fibonacci(2)) # 1
print(fibonacci(6)) # 8
print(fibonacci(7)) # 13