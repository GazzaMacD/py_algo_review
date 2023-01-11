def strong(func):
    def wrapper():
        return f"<strong>{func()}</strong>"

    return wrapper


@strong
def hello():
    return "Hello from Zim"


print(hello())


def trace(func):
    def wrapper(*args, **kwargs):
        print(f"Trace: calling {func.__name__}() " f"with {args}, {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"Trace: {func.__name__}() " f"returned {original_result}")
        return original_result

    return wrapper


@trace
def say(name, phrase):
    return f'{name}  says "{phrase}"'


say(name="Bob", phrase="Hi there")

"""
In order to retain the wrapped function meta 
data used the functools.wraps decorator
"""
import functools


def wrap(func):
    @functools.wraps(func)
    def wrapper():
        return func()

    return wrapper


@wrap
def baz():
    """Returns a useless string"""
    return "baz is a silly name for a function"


# meta data retained
print(baz.__doc__)
print(baz.__name__)
