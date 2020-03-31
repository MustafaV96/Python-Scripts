def encrypt(word):
	cipher = ""
	
	for i in word[::-1]:
		cipher = cipher + i
	
	cipher = cipher.replace('a', '0')
	cipher = cipher.replace('e', '1')
	cipher = cipher.replace('o', '2')
	cipher = cipher.replace('u', '3')
		
	cipher = cipher + 'aca'
	
	return cipher
