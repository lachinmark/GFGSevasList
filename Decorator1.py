# Create a decorator named time_function that measures the time it takes for a function to execute and prints the duration.

import time

def time_function(func):
    def wrap():
        before = time.time()
        func()
        after = time.time()
        print(f'Time spent on execution : {after - before}')
    return wrap

@time_function
def slow_function():
    time.sleep(2)

# Test the decorator
slow_function()