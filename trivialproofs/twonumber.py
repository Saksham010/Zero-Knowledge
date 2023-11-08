# Claim "I know two value x and y such that x+y = 15"

#Proof: 
from py_ecc.bn128 import G1,multiply,add

#Prover

secret_x = 7
secret_y = 0

coeff_x = 23
coeff_y = 1

A = multiply(multiply(G1,secret_x),coeff_x)
B = multiply(multiply(G1,secret_y),coeff_y)

proof = (A,B,161)


#Verifier

if(multiply(G1,proof[2]) == add(proof[0],proof[1])):
    print("Valid proof")

else:
    print("Invalid proof")
