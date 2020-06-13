import sys

#print(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])




# numbers_list = map(int, input().split())
# print("numbers_list",numbers_list)
# for num in numbers_list:
#     print(num)

no_airport, start_airport,  dest_airport = map(int, input().split())



airport_string  = input()

if airport_string[start_airport-1] == airport_string[dest_airport-1]:
    print(0)
else:
    print(1)