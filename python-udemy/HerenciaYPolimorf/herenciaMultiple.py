class A:
    def __init__(self):
        super().__init__()
        print("Soy clase A")
    
    def a(self):
        print("Metodo A clase A")

class B:
    def __init__(self):
        super().__init__()
        print("Soy clase B")
    
    def  b(self):
        print("Metodo B clase B")

class C(A,B):
    def c(self):
        print("Metodo C clase C")

c=C()

c.c()