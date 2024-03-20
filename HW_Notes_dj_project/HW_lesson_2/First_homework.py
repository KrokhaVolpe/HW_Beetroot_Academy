#class Foo(object):
#
#    def __new__(cls):
#        if not hasattr(cls, 'instance'):
#           cls.instance = super(Foo, cls).__new__(cls)
#            print("Instance")
#        return cls.instance
#
#foo1, foo2, foo3 = Foo(), Foo(), Foo()



#x, y, *z = 1, 2, 3, 4, 5
#print(x, y, *z)

#class A:
#    def __init__(self, i=100):
#        self.i=i

#class B(A):
#     def __init__(self, j=0):
#        self.j=j

#def main():
#    b = B()
#    print(b.i)
#    print(b.j)

#main()


num = [1, 2, 3, 4, 5]
mapped = list(map(lambda x: x * 2, num))
filtered = list(filter(lambda x: x % 3 == 0, mapped))
print(filtered)
