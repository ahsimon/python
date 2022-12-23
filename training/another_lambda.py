is_even_list = [lambda arg=x: arg * 10 for x in range(1, 500)]

# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
	print(item())



# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))

print(adults)

