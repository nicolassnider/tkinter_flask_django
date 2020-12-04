def suma(a,b):
    return a+b


def resta(a,b):
    return a-b

def ArgsUndef(*args):
    for dato in args:
        print (dato)

def ArgsByName(**kwargs):
    print(kwargs)
    
def cuenta_regresiva(n):
    print(n)
    n-=1
    if n>0:
        cuenta_regresiva(n)
        
    else:
        print("llegó a 0")

n=10000
cuenta_regresiva(n)       
    
#s=suma(2,1)
#print(s)

#print(resta(b=4,a=1))

#print(ArgsUndef("a",4,{"q","r",1,2,5.4}))
#print(ArgsByName(a=resta(2,3),b="asd",c=123,d="12-01-1990"))