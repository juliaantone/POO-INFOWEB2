x = []
y = list()
z = [1, 2, 3, 4]
x.append(10)
print(type(x), len(x), (x))
print(type(y), len(y), (y))
print(type(z), len(z), (z))
print(z[0])
print(*z)
#print(z[4])
#print(int("teste"))
#print(1/0)

print( "-" * 50)

j = [10, 5, 15, 20]
for v in j:
    print(v)

print( "-" * 50)

for c in "ANTONELLY":
    print(c)

print( "-" * 50) 

i = 0 
while i < len(j):
    print(j[i])
    i = i + 1
