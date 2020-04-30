# precomputation allowed. 
import math as mt 
  
MAXN = 100001
  
# list storing smallest prime factor for every number from 0 to 100001
spf = [0 for i in range(MAXN)] 

#we will be using this same array for all the elements whose prime factorisation has to be calculated, hence we can consider this as a preprocessing task.

for i in range(1,len(spf)):
    spf[i]=i


for i in range(2, len(spf)):
    if spf[i] == i:
        for j in range(i*i, MAXN, i):
            if spf[j]%i == 0:
                spf[j] = i

prime_factor = []
print(spf[12246]) 
#now we create a method for using this array
def prime_factorization(num):
    while(num!=1):
        prime_factor.append(spf[num])
        num = num //spf[num]
    return prime_factor 

list_factors = prime_factorization(12246)

for i in range(len(list_factors)):
    print(list_factors[i])