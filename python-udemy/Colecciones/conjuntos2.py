c1={1,2,3}
c2={3,4,5}

c3=c1.union(c2)
print(c3)
c1.update(c2)
print(c1)

c1={1,2,3}
print(c1.difference(c2))

c1={1,2,3}
c2={3,4,5}

c3=c1.intersection(c2)
print(c3)

c3=c1.symmetric_difference(c2)
print(c3)