import time

def timer(fun):
 
    def inner(*args):
        t0 = time.time()
        result = fun(*args)
        t1 = time.time()
 
        print(f"I did {fun.__name__} and it took me: {(t1 - t0) * 1000} miliseconds")
        return result
 
    return inner

