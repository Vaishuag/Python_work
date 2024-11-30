def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments {args} and {kwargs}.")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        print('')
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def sub(a, b):
    return a - b


# Call the decorated function
add(5, 3)
sub(23,15)
