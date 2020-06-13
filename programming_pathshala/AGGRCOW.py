#put your header file if needed

#function to check if the cows can fir in the barn
def fit(list_val,dist,n_cows):
	n_cows -= 1
	#print(n_cows)
	begin = list_val[0]
	for i in range(1,len(list_val)):
		if (list_val[i]-begin) >= dist:
			n_cows-=1
			begin = list_val[i]
			i+=1
	###print(n_cows)
		if n_cows == 0:
			return True
	return False
	
			
		
#binary search function
def binary_search(list_val, n_cows):
	max_dist = list_val[len(list_val)-1] - list_val[0]
	min_dist = float('inf')
	for i in range(len(list_val)-1):
		min_dist = min((list_val[i+1]-list_val[i]),min_dist)
	#print(max_dist, min_dist)
	while(min_dist<=max_dist):
		mid = (max_dist+min_dist)//2
		#print("calculation",mid)
		if fit(list_val,mid,n_cows):
			if fit(list_val,mid+1,n_cows):
				min_dist = mid+1
			else:
				#print(mid)				
				return mid
		else:
			max_dist = mid - 1
	#print("here")

#first we take the input about how many numbers of test cases we have to run
number_test = int(input())
#print("number_test",number_test)
for i in range(number_test):
	list_val = []
	len_arry, n_cows = map(int, input().split())
	#print("len_array",len_arry)
	for j in range(len_arry):
		val  = int(input())
		list_val.append(val)
	list_val = sorted(list_val)
	#print(list_val)
	print(binary_search(list_val,n_cows))
