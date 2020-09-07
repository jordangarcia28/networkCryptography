def main():
	myMessage = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
	myKey = 2
	ciphertext = encryptMessage(myKey, myMessage)
	print (ciphertext)


def encryptMessage(key, message):
	ciphertext = [''] * key

	for col in range(key):
		pointer=col

		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()