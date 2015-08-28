#------------------------------------------
#Ransom Note from Magazine, Kidnapper kidnaps you and 
#writes a ransom note. He does not write it with hand, 
#as handwriting can put him in, so reaches to a magazine 
#at table and creates ransom note. We need to find out given 
#ransom string and magazine string, is it possible to create given 
#ransom note. Kidnapper can use individual characters of words.
#------------------------------------------

 #Str1 is the ransom note, Str2 is the string from magazine

def ransomNote(str1,str2):
 	strTable = []
 	for i in range(0,255):
 		strTable.append(0)
 	i = 0
 	while i < len(str2):
 		strTable[ord(str2[i])] += 1
 		i += 1
 	j = 0
 	#print strTable
 	while j < len(str1):
 		strTable[ord(str1[j])] -= 1
 		if strTable[ord(str1[j])] < 0:
 			return False
 		j += 1
 	return True

str1="I love you"
str2="I don't love you"
print ransomNote(str1,str2)