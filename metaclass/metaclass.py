class MyMeta(type):
    def __new__(cls, name, bases, namespace, **kwds):
        print('__new__', cls, name, bases, namespace)
        result = type.__new__(cls, name, bases, namespace)
        return result

class MyClass(metaclass=MyMeta):
    def __new__(cls, num):
        print('__new__', cls, num)
        return super().__new__(cls)

    def __init__(self, num):
        self.num = num

print(MyClass(5))
