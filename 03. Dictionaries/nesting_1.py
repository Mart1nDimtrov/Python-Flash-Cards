#Store a collection of dictionaries in a
#list.

musicians = []

e_fitzgerald = {
	'first': 'Ella',
	'last': 'Fitzgerald',
}
musicians.append(e_fitzgerald)

j_joplin = {
	'first': 'Janis',
	'last': 'Joplin',
}
musicians.append(j_joplin)

for musician in musicians:
	full_name = musician['first']
	full_name += ' ' + musician['last']
	print(full_name)