# Recursive Solution.
def recursive(numArg):
    # Performance diff? -> numArg < 2 
    # (still runs correctly but the f(2) = 1 comes from the outer else statement not the initial check)
    if numArg <= 2: 
        if numArg == 1 or numArg == 2:
            return 1
        elif numArg == 0:
            return 0
        else:
             return "Error. Must be a positive number."
    else:
        return (fibonacci(numArg-1) + fibonacci(numArg-2))
    
# For Loop Solutions. 
def for_loop(numArg):
   
    # Initial Variables
    first_in_series = 0 # first number
    second_in_series =  1   # second number in fib series
    current_result = 2
    
    for i in range(1, numArg, 1):
        # update result
        current_result = first_in_series + second_in_series   # NOTE -> bug if wrong variable
        # update variables
        first_in_series, second_in_series = second_in_series, current_result
    
    return f'For Loop: {current_result}'
    
# While Loop Solutions.     
def while_loop(numArg):
    if numArg <= 2:
        return 1 if numArg in {1,2} else 0  # doesnt work for negative numbers yet
    else:
        first_in_series = 0     # first number
        second_in_series =  1   # second number in fib series

        while numArg > 1 :
            # update result
            current_result = first_in_series + second_in_series   # NOTE -> bug if wrong variable
             # update variables
            first_in_series, second_in_series = second_in_series, current_result
            numArg -= 1
        
        return f'While Loop: {current_result}'

# Main fib function that is initially called.        
def fibonacci(numArg, loop_type):
    # Check numArg initially incase it is 0 or 1
    # Add upper limit here of 10000 (add another zero and runtime error is thrown.)
    if numArg <= 2:
        if numArg in {1,2}:
            return 1
        elif numArg == 0:
            return 0
        else:
            return "Error. Negative number."
    else:
        match loop_type:
            case 'WHILE': return while_loop(numArg)
            case 'FOR': return for_loop(numArg)
            case _ : return recursive(numArg)

print(fibonacci(-1, 'FOR')) # ERROR.
print(fibonacci(0, 'WHILE')) # 0
print(fibonacci(1, 'WHILE')) # 1
print(fibonacci(2, 'WHILE')) # 1
print(fibonacci(6, 'FOR')) # 8
print(fibonacci(10000, 'WHILE')) # 13