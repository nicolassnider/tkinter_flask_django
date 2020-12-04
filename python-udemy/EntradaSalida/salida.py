v = "otroTexto"

n= 10

c= "un Texto '{v}' y un numero '{n}'".format(v=v,n=n)

print(c)

print("{:>30}".format("palabra"))
print("{:30}".format("palabra"))
print("{:^30}".format("palabra"))

print("{:.3}".format("palabra"))

print("{:>30.3}".format("palabra"))

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

c = "{:06d}".format(1234)
print(c)


