from py_ecc.bn128 import G1, G2, pairing, add,multiply,eq

a = 5
b = 6
c = 5*6

A = multiply(G2,a)
B = multiply(G1,b)
C = multiply(G2,c)

print(eq(pairing(A,B),pairing(C,G1)))
