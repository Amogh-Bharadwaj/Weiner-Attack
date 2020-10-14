import math
from Cryptodome.Util.number import *
from sage.all import *

# N = ?
# e = ?
# c = ?
def continued_fractions(a, b):
    cf = []
    while b != 1:
        cf.append(a//b)
        temp = a
        a = b
        b = temp % b
    cf.append(a)
    return cf
    
a = continued_fractions(e, N)


k = [a[0], a[1]*a[0] + 1]
d = [1, a[1]]
for n in range(2, len(a)):
        k.append(a[n]*k[n - 1] + k[n - 2])
        d.append(a[n]*d[n - 1] + d[n - 2])
    
for i in range(len(k)):
        try:
         if (e*d[i] - 1) % k[i] == 0:
           phi = (e*d[i] - 1)//k[i] 
           x = PolynomialRing(RationalField(), 'x').gen()
           f = (x**2) - (N - phi + 1)*x + N
           n_factors = f.roots()
           if n_factors[0][0]*n_factors[1][0] == N:
               print("Message Cracked!")
               print(long_to_bytes(pow(c,d[i], N)))
               break
        except:
            continue
