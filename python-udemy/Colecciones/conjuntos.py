conjunto=set()

conjunto.add(1)
conjunto.add(2)
conjunto.add(3)
conjunto.add(4)

#print(conjunto)

conjunto.discard(1) 

#print(conjunto)

# comparacion de conjuntos
c1={1,2,3}
c2={4,5,6}
c3={1,2,3,4,5}
c4={1,2,3,4,5,6,7}

print(c1.isdisjoint(c2)) 

print(c3.issubset(c4)) 

print(c4.issuperset(c4)) 