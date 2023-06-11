# Que 2 :
# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.
#The function should return 0 if a non-integer is passed in.


def add_it_up(n):
	sum = 0
	if type(n)==type(sum):
		for num in range(1,n+1):
			sum = sum + num
		print("Sum is : ",end="" )
		return sum
	else:
		print("Input is Not an Integer Value ! ")
		return 0

print(add_it_up(2))