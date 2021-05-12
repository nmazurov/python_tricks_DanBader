from string import Template
import functools


def getDiscount(price, discount):
    newPrice = price * (1 - discount)
    assert 0 <= newPrice <= price
    return newPrice


def array_madness(a, b):
    sum_a = 0
    sum_b = 0
    for el in a:
        sum_a += el ** 2
    for el in b:
        sum_b += el ** 3

    if sum_a > sum_b:
        return True;
    return False


def array_madness2(a, b):
    return sum(x ** 2 for x in a) > sum(x ** 3 for x in b)


a = [1, 2, 3]
b = [1, 1, 2]


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


class Test:
    def __init__(self):
        self.foo = '1'
        self._bar = '2'
        self.__baz = '3'


class TestExt(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'over1'
        self._bar = 'over2'


print(array_madness2(a, b))

with ManagedFile('d:\dsa.txt') as f:
    f.write('dsa22')

with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')

t = TestExt()


def yell(text):
    return text.upper() + '!'


print(t.foo, t._bar, t._Test__baz)
print(dir(t))

templ_string = 'Hey $name, there is a $error error!'
print(Template(templ_string).substitute(name='КОля', error='dsa'))

bark = yell
print(bark('fds'))
print(bark.__name__)

func = [bark, str.lower, str.capitalize]

for f in func:
    print(f, f('DsA'))

print(list(map(bark, ['hello', 'hey', 'hi'])))


def func1(text):
    def func2(text):
        return text * 2

    return func2(text) + '1'


print(func1('dsa'))

print((lambda x, y: x + y * 2)(2, 3))


def null_decorator(func):
    return func


@null_decorator
def sum(a, b):
    return a + b


sum2 = null_decorator(sum)
print(sum(2, 4))


def uppercase(func):
    def wrapper(x):
        original_result = func(x)
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def strong(func):
    def wrapper(x):
        modified_result = '<b>' + func(x) + '</b>'
        return modified_result

    return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result

    return wrapper


@trace
@strong
@uppercase
def simple_func(x):
    return x + 'xhdfghs'


print(simple_func('dsa'))


def sum(*args):
    print(args)
    s = 0
    for n in args:
        s += n
    return s


print(sum(1, 2, 3, 4, 5))


def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(1, 2, 3)
l = [11, 2, 3]
t = (1, 22, 33)
genexpr = (x * x for x in range(2, 7))
dict_vec = {'y': 0, 'z': 1, 'x': 2}

print_vector(*l)
print_vector(*t)

print(*l)
print(*t)
print(*genexpr)

print(*dict_vec)
print_vector(**dict_vec)


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
    if len(name)<10:
        raise NameTooShortError(name)

#validate("Коля")

import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
zs = copy.deepcopy(xs)
xs.append([10,11])
ys[1][1] = 'dsa'
xs[0][1] = 'fff'

print(xs)
print(ys)
print(zs)
