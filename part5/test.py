
stuff = ('hello', 'world', 'bye', 'now')
stuff_list = list(stuff)
index = stuff_list.index('bye')
stuff_list[index] = 'goodbye'
stuff = tuple(stuff_list)
print(stuff)