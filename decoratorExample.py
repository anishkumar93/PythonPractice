


def decorator_function(func):
    def wrapper():
        print("function got wrapped")
        func()
    return wrapper



@decorator_function
def simple_function():
    print("Iam a simple function")


# simple_function()


def smart_divide(func):
    def wrapper(a,b):
        print("gonna divide a and b")
        if b == 0:
            print("Cannot be divided")
            return
        return func(a,b)
    return wrapper

@smart_divide
def divide(a,b):
    print(a/b)


# divide(4,0)


def chain_decorators(func):

    def wrapper(*args, **kwargs):
        print('%' * 30)
        func(*args, **kwargs)
        print('%' * 30)
    return wrapper

def chain2_decorator(func):
    def wrapper(*args, **kwargs):
        print('*' * 30)
        func(*args, **kwargs)
        print('*' * 30)
    return wrapper

@chain_decorators
@chain2_decorator
def hello(msg):
    print(msg)

hello('Hello')
