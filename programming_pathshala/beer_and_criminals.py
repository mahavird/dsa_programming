#first we need to take inputs from the user:

#The first line of the input contains two integers n and a (1 ≤ a ≤ n ≤ 100) — the number of cities and the index of city where Limak lives.

#The second line contains n integers t 1, t 2, ..., t n (0 ≤ t i ≤ 1). There are t i criminals in the i-th city.

n, a = map(int, input().split())

numbers_list = map(int, input().split())
criminals_city = []
#print("numbers_list",numbers_list)
for num in numbers_list:
    criminals_city.append(num)



    

def count_criminals(criminals_city):
    count =0

    if len(criminals_city) == 1:
        if criminals_city[0]:
            print(1)
        else:
            print(0)
        return 


    if criminals_city[a-1] == 1:
        count+=1


    min_val = min(n-a, a-1)
    val_n = n
    #print(a-1)
    left_val = a-1
    for i in range(1, min_val+1):
        #print(a-1-i,a-1+i)
        if criminals_city[a-1-i] == 1 and criminals_city[a-1+i] == 1:
            count+=2
        left_val = a-1-i 
    #print(a-1-i)
    #print(left_val)
    if left_val !=0:
        #print(val_n)
        for i in range(left_val):
            #print(i)
            if criminals_city[i] == 1:
                count+=1
    #print("count so far", count)
    for i in range(a+min_val,n):
        #print(i)
        if criminals_city[i] == 1:
            count+=1
    print(count)
    #return count

count_criminals(criminals_city)