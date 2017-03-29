import pygame

class A:
    x = 'x'

    def __init__(self):
        print("New class A")
        self.y = 'y'

    z = 'z'

class B(A):
    def __init__(self):
        A.__init__(self)
        print("New class B")

a = A()
b = B()

print "---------"

print b.y
