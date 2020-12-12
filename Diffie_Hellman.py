# Program Code by Akash
from random import randint
 
P = int(input("Enter prime number here --> "))
     
G = int(input("Enter primitive root here --> "))
     
print('The Value of P is :%d'%(P))
print('The Value of G is :%d'%(G))
     
# Akash will choose the private key a 

a = int(input("Enter 1st private key here(a) --> "))

if a < P:
    print('The private Key a for Akash is :%d'%(a))
 
else:
    print('You are entered wrong private key value, private key value should be less than the prime number.')
    exit()


x = int(pow(G,a,P))  
     
# Tanvi will choose the private key b
b = int(input("Enter 2nd private key here(b) --> "))
if b < P:
    print('The private Key b for Tanash is :%d'%(b))
else:
    print('You are entered wrong private key value, private key value should be less than the prime number.')
    exit()


y = int(pow(G,b,P))
 
# Secret key for Akash
ka = int(pow(y,a,P))
    
# Secret key for Tanash
kt = int(pow(x,b,P))

print('Public key for the Akash is : %d'%(x)) 
print('Public key for the Tanash is : %d'%(y))
print('Secret key for the Akash is : %d'%(ka))
print('Secret Key for the Tanash is : %d'%(kt))
