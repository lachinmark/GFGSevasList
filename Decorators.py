# Create a decorator named log_function_call that logs the name and arguments of a function every time it is called.

def log_function_call(func):
    def wrapper(*args):
        # Log the function name and arguments
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments ")
        result = func(*args)
        # Log the function result
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper


@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

@log_function_call
def add(a, b):
    return a + b

# Test the decorator
say_hello("Alice")
print(add(5, 3))