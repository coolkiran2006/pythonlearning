'''Syntax:
	string_name[lower_index:upper_index]
'''
string="python"
length=int(len(string))
for i in range(length):
	print(string[i])
for i in range(1,len(string)+ 1):
	print(string[-i])

