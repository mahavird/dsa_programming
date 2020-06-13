# your code goes here
no_of_val = int(input())

list_val = []
for i in range(no_of_val):
	list_val.append(int(input()))

dict_value_left = {}
dict_value_right = {}
for a in range(len(list_val)):
	for b in range(len(list_val)):
		for c in range(len(list_val)):
			value = list_val[a]*list_val[b] + list_val[c]
			if value in dict_value_left:
				dict_value_left[value]+=1
			else:
				dict_value_left[value]=1
for d in range(len(list_val)):
	if d == 0:
		continue
	for e in range(len(list_val)):
		for f in range(len(list_val)):
			value = list_val[d]*(list_val[e] + list_val[f])
			if value in dict_value_right:
				dict_value_right[value]+=1
			else:
				dict_value_right[value]=1
count=0
for key,values in dict_value_left.items():
	if key in dict_value_right:
		count+=values*dict_value_right[key]

			

print(list_val)
print(dict_value_left)
print(dict_value_right)
print(count)