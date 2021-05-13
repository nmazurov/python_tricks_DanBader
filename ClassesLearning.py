class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def to_string(self):
        print(self.color, self.model)

    def __str__(self):
        return f'{self.color} {self.model}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.color!r}, {self.model!r})')

    def __repr1__(self):
        return f'repr: {self.color} {self.model}'


c = Car("Зеленый", "Киа")
c.to_string()
print(c)
print(repr(c))
print(c.__repr__())

import datetime

today = datetime.date.today()
print(today)


class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


# validate("Коля")

import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
zs = copy.deepcopy(xs)
xs.append([10, 11])
ys[1][1] = 'dsa'
xs[0][1] = 'fff'

print(xs)
print(ys)
print(zs)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


p1 = Point(11, 22)
p2 = copy.copy(p1)

print(p1)
print(p2)


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


rect = Rectangle(Point(0, 1), Point(5, 6))
# srect = copy.copy(rect)
srect = copy.deepcopy(rect)
print(rect, srect)

rect.bottomright = Point(0, 0)
print(rect, srect)

rect.topleft.x = -2
print(rect, srect)

rect.bottomright.x = -5
print(rect, srect)

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def __init__(self):
        self.p = '123'
    def foo(self):
        self.p = '456'
    def bar(self):
        self.p = '1456'

#b = Base()
c = Concrete()
c.foo()
c.bar()
print(c.p)

tup = ('hello', object(), 42)
print(tup)

from collections import namedtuple
Car = namedtuple('Carrr' , 'color mileage')

c = Car('dsa', 123)
print(c)
d = Car('dsa', '1235')
print(*d)

#subclass from namedtuple
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
e = ElectricCar('Red', 555, 45)
print(d._asdict())
print(e._asdict())

#Class vs Instance Variable Pitfalls

class Dog:
    num_legs = 4 # <- Class variable
    def __init__(self, name):
        self.name = name

jack = Dog('Jack')
jill = Dog('Jill')

jill.num_legs = 7
Dog.num_legs = 6

print((jack.name, jill.name, jack.num_legs, jill.num_legs, Dog.num_legs))


class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances += 1

c1 = CountedObject()
c2 = CountedObject()
print(c1.num_instances,c2.num_instances, CountedObject.num_instances)
