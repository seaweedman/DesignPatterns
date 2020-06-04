'''
prototype
原型模式
定义：用一个已经创建的实例作为原型，
通过复制该模型对象来创建一个和原型相同或相似的新对象。

实现方式：浅拷贝、深拷贝
'''
import copy

class Prototype:
    # 浅拷贝
    def shallowClone(self):
        return copy.copy(self)

    # 深拷贝
    def deepClone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    a = Prototype()
    b = a.shallowClone()
    c = a.deepClone()
    print(id(a), id(b), id(c))
