#Make a copy of a list by using a slice 
#from start to end.
states = ['CA', 'CO', 'CT', 'DE', 'FL', 'GA']
my_states = states[:]
my_states.append('MN')
print(states)
print(my_states)