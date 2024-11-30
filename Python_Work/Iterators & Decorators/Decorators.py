# decorator

def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator  #  greet = my_decorator(hello)
def greet():
    print("Hello, Vaishnavi!")

# Call the decorated function
greet()
