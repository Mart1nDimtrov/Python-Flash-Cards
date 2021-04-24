#The range() generates a series of numbers.
nums = list(range(5))
print(nums)

#Pass two numbers as arguments to create a range
#that starts with the first and ends with one less
#than the second values.
high_nums = list(range(95, 100))
print(high_nums)

#To skip pass a third argument.
odds = list(range(1, 10, 2))
print(odds)

#Define a pattern.
nums = []
for exp in range(5):
	nums.append(10**exp)

print(nums)
