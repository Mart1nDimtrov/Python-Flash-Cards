#A while loop runs as long as a condition is true:
num = 0

while num < 3:
	print(num)
	num+=1

#A while with a list runs until the list is empty:
nums = [1,2,3,5]
while nums:
	print(nums.pop())

#Another example.
bugs = ['bug 1', 'bug 2', 'bug 3']
while bugs:
	bug = bugs.pop()
	print(f"Fixing {bug}.")
print("All bugs fixed!")