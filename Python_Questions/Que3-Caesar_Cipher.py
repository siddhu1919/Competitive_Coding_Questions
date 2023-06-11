# Que 3 : Caesar Cipher 
# A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. For example, assume the input plain text is the following:

# abcd xyz

#If the shift value, n, is 4, then the encrypted text would be the following:

# efgh bcd

# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

# Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

plain_text = "Im Sidvwxyz"

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_len = len(alpha) - 1

#Helper code 

#print(alpha[21:]+alpha[:21])
#print(alpha.index('w'))
#print(alpha_len)

#Caesar Function 

def caesar_Cipher(plain_txt,shift_num=4):
	# 1 Converting Txt In Lower Case
	plain_txt = plain_txt.lower().replace(" ","")
	
	print(plain_txt)
	# 2 Masking/Transcoding The Plain Txt
	cipher = ""
	for letter in plain_txt:
		if alpha.index(letter)>21:
			temp_alpha = alpha[alpha.index(letter):]+ alpha[:alpha.index(letter)]
			cipher += temp_alpha[temp_alpha.index(letter)+shift_num]
		else:
			cipher += alpha[alpha.index(letter)+shift_num]
	print(cipher)
		
	
	

caesar_Cipher(plain_text)