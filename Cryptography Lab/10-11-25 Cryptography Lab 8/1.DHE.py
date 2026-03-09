P = 23
G = 9
print("Value of P is:", P) 
print("Value of G is:", G)

a = int(input("Enter Private key for Alice: "))
# print('The Private Key a for Alice is :%d'%(a))
x = int(pow(G,a,P))


b = int(input("Enter Private key for Bob: "))
# print('The Private Key b for Bob is :%d'%(b))
y = int(pow(G,b,P))

ka = int(pow(y,a,P))
kb = int(pow(x,b,P))
print('Secret key for the Alice is : %d'%(ka))
print('Secret Key for the Bob is : %d'%(kb))
