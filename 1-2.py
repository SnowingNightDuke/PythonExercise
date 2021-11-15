# import beautifulsoup4 
def recursive(c, b):
    r = Calculator(c,b)
    print("addtion:" + str(r.addition()))
    print("division:" + str(r.division()))
    print("multiplication:" + str(r.multiplication()))
    print("subtraction:" + str(r.subtraction()))
    r.p()
    
    
    

class Calculator:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def addition(self) -> int:
        return int(self.a + self.b)
    def multiplication(self) -> int:
        return self.a * self.b
    def division(self) -> float:
        return int(self.a/self.b)
    def subtraction(self) -> int:
        return self.a - self.b
    def p(self):
        
        s=type(self.a)
        k = type (self.b)
        print(s)
        print(k)

a:int = input("please input a\n")
b:int = input("please input b\n")
recursive(a,b)