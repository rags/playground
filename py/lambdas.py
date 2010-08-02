class Foo:
    def __init__(self):
        self.x=10

def main():
    y=Foo()
    print foo(lambda x: x>y.x,12)
def foo(fn,param):
    return fn(param)
    
if __name__=='__main__':
    main()    
