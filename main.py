import os

# lamda example
def lambda_example():
    say_hi = lambda name : f'Hello {name}'
    print(say_hi('matt'))

# Working with files
def os_example():
    cwd = os.getcwd() # returns the current working directory
    print(cwd)


