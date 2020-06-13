string = "cab"
string  = sorted(string)
n = len(string) 
 
def helper(index , curr ): 

	# base case 
	if index == n: 
		return

	if len(curr) > 0: 
		print(curr) 

	for i in range( n): 
		helper(i, curr+string[i] ) 



helper(0,"")


