'''
singleton
单例模式
定义：一个类只有一个实例，且该类能自行创建这个实例。

实现方式：懒汉式、饿汉式
'''
class A(object):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

if __name__ == "__main__":
    a1 = A()
    a2 = A()

    print(id(a1), id(a2))
