def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for stop_word in words:
                stop_word = stop_word.append("*")
                return stop_word
            return wrapper
        return decorator



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called {args}, {kwargs}")
        return func(*args, **kwargs)
    
    return wrapper

@logger
def add(x, y):
        return x + y

@logger
def sguare_all(*args):
    return[arg ** 2 for arg in args]


add(4, 5)
sguare_all(10, 15 ,20)
