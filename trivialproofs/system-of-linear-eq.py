from py_ecc.bn128 import G1,multiply,add,FQ,neg

# x + y = 5
# 2x - y = 1


#Prover
x = 2
y = 3

coeff_x_one = 1
coeff_y_one = 1
output_one = 5

coeff_x_two = 2
coeff_y_two = neg(multiply(G1,1))
output_two = 1


mulx = multiply(G1,x)
muly = multiply(G1,y)

secret_x_one = multiply(mulx,coeff_x_one)
secret_y_one = multiply(muly,coeff_y_one)

secret_x_two = multiply(mulx,coeff_x_two)
secret_x_two = multiply(muly,coeff_y_two)

secret_x = multiply(secret_x_one,secret_x_two)
secret_y = multiply(secret_x_two,secret_y_two)

combined_output = multiply(multiply(G1,output_one),output_two)

proof = (secret_x,secret_y,combined_output)


#Verifier

print(proof)



