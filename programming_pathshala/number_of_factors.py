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
res = 1

#now we create a method for using this array
def prime_factor_count(num):
    res=1
    count = 1
    while(num!=1):
        #prime_factor.append(spf[num])
        fact = spf[num]
        num = num //spf[num]
        if fact ==  spf[num]:
            count+=1
        else:
            res = res*(count+1)
            count=1 
    return res



list_numbers = [10, 30, 100, 450, 987]
for i in range(len(list_numbers)):
    print("total prime factors", prime_factor_count(list_numbers[i]))


# number of elemetns as input 

n = int(input("Enter number of elements : "))

arr_ex= []
# iterating till the range 
for i in range(0, n): 
    val = int(input())
    arr_ex.append(val) # adding the elem
for i in range(len(arr_ex)):
    print("total prime factors", prime_factor_count(arr_ex[i]))