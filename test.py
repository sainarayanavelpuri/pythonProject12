import demo
a=200
def func():
    print("in func of test")
if __name__=="__main__":
    print(a)
    func()
    print(demo.p)
    demo.myfunc()
    print("test module name is:",__name__)
    print(dir(a))
