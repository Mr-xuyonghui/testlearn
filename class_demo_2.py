class A:
    def play(self):
        print("This ia A")
class B(A):
    def play(self):
        print("This ia B")
class C(B):
    def play(self):
        print("This ia C")
class D(C):
    def play(self):
        print("This ia D")

d=D()
d.play()
print(d.__mro__)