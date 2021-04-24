#A list comprehension is a compact way of 
#defining a list in one line.
nums = [10**exp for exp in range(5)]
print(nums)

#Modify an existing list.
states = ['CA', 'CO', 'CT']
lower_states = [state.lower() for state in states]
print(lower_states)