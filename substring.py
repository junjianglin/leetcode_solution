#----------------------
#   Implementation of substring,   brute force,  str1 is substring of str2
#----------------------

def substring(str1,str2):
	l = len(str1)
	if l == 0:
		return True
	if len(str2) == 0:
		return False
	match = False
	i = 0
	while i < len(str2) - l + 1:
		j = 0
		while j < l:
			if str1[j] == str2[i+j]:
				match = True
			else:
				match = False
				break
			j += 1
		if match == True:
			return True
		i += 1
	return False


a = "abcd"
b = "abcefg"
print substring(a,b)
