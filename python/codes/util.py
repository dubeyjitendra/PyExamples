import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        #print("last ",end - start)
        print(func.__name__+" took "+str((end - start) * 1000) + " mili sec")
        return result
    return wrapper

