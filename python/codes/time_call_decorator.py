import time
def time_call(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(func.__name__ + " took " + str(end_time - start_time))
        return result
    return wrapper



## timing
## logging
## authentication


# @auth
# @log
@time_call
def cal_sql(n):
    lst=[]
    for i in n:
        lst.append(i*i)
    return lst

@time_call
def cal_cube(n):
    lst=[]
    for i in n:
        lst.append(i*i*i)
    return lst


value= range(100000)
cal_sql(value)
cal_cube(value)