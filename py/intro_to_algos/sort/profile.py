import timeit

def profile(func):
    def wrap(*args,**kwargs):
        ret = None
        def time():
            ret = func(*args,**kwargs)
        print timeit.Timer(time).timeit(1)
        return ret
    return wrap
