'''
factory method
工厂方法
定义：定义一个创建产品对象的工厂接口，
将产品对象的实际创建工作推迟到具体子工厂类当中。
'''
import abc

# 抽象产品类
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def draw(self):
        pass

    def getShape(self):
        return self.shape_name

class Circle(Shape):
    def __init__(self):
        self.shape_name = "Circle"

    def draw(self):
        print("draw circle")

class Rectangle(Shape):
    def __init__(self):
        self.shape_name = "Rectangle"

    def draw(self):
        print("draw rectangle")

# 抽象工厂类
class ShapeFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self):
        pass

class CircleFactory(ShapeFactory):
    def create(self):
        return Circle()

class RectangleFactory(ShapeFactory):
    def create(self):
        return Rectangle()

if __name__ == "__main__":
    factory = CircleFactory()
    circle = factory.create()
    print(circle.getShape())
    circle.draw()

    factory = RectangleFactory()
    rectangle = factory.create()
    print(rectangle.getShape())
    rectangle.draw()
