# your code goes here
import sys



def rearrange_helper(arr_ex, i):
	val_help = -(i+1)
	#print("i is over here", i)

	i = arr_ex[i]-1
	#print("arr_ex[i]",arr_ex[i])

	while(arr_ex[i]>0):
		#print("arr_ex[i] in while",arr_ex[i])

		new_i = arr_ex[i] - 1
		arr_ex[i] = val_help
		val_help = -(i+1)
		i = new_i
		#print("i here is" , i)



def rearrange(arr_ex):
	for i in range(len(arr_ex)):
		arr_ex[i] = arr_ex[i]+1
	for i in range(len(arr_ex)):
		if arr_ex[i]>0:
			rearrange_helper(arr_ex,i)
	for i in range(len(arr_ex)):
		arr_ex[i] = (-arr_ex[i])-1 


def print_array(arr_ex):
	for i in range(len_array):
		print(arr_ex[i])

#arr_ex = [2,0,1,4,5,3]
# creating an empty list 
arr_ex = []


# number of elemetns as input 
n = int(input("Enter number of elements : "))


# iterating till the range 
for i in range(0, n): 
    val = int(input()) 
  
    arr_ex.append(val) # adding the element 

len_array = len(arr_ex)
#print_array(arr_ex)
print(arr_ex)

rearrange(arr_ex)
print(arr_ex)
