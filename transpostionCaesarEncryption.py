import os, sys, math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encrypt_caesar(key, message):
    global SYMBOLS
    result= ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            resultIndex = symbolIndex + key
            
            if resultIndex >= len(SYMBOLS):
                resultIndex = resultIndex - len(SYMBOLS)
            elif resultIndex < 0:
                resultIndex = resultIndex + len(SYMBOLS)

            result = result + SYMBOLS[resultIndex]
        else:
            result = result + symbol


    return result

def encrypt_transposition(key, message):
	ciphertext = [''] * key
	for col in range(key):
		pointer=col

		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
			
	return ''.join(ciphertext)

def main_encrypt():

    key = 8


    while(1):
        mode = input("Caesar(c) atau Transposition(t) ?: ")
        mode = mode.lower()
        if (mode == 'c'):
            break
        elif (mode == 't'):
            break

    
    file = ("dracula.txt")
        
    if not os.path.exists(file):
        print('[*]The file %s does not exist. Quitting...' %(file))
        sys.exit()    

    inputFile = file

    outputFile = os.path.splitext(file)[0]
    if(mode == 'c'):
        outputFile=outputFile+'.caesar.encrypted.txt'
    elif (mode == 't'):
        outputFile=outputFile+'.transposition.encrypted.txt'

    file = open(inputFile)
    message = file.read()
    file.close()

    print('processing...' )


    if mode == 'c':
        result = encrypt_caesar(key, message)
    elif mode == 't':
        ciphertext = encrypt_transposition(key, message)
        result = ciphertext



    file = open(outputFile, 'w')
    file.write(result)
    file.close()

    print('output file is %s' % (outputFile))


def decrypt_caesar(key, message):
    global SYMBOLS
    result= ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            resultIndex = symbolIndex - key
            
            if resultIndex >= len(SYMBOLS):
                resultIndex = resultIndex - len(SYMBOLS)
            elif resultIndex < 0:
                resultIndex = resultIndex + len(SYMBOLS)

            result = result + SYMBOLS[resultIndex]
        else:
            result = result + symbol


    return result

def decrypt_transposition(key, message):
    global SYMBOLS

    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    result = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        result[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(result)


def main_decrypt():

    key = 8


    while(1):
        mode = input("Caesar(c) atau Transposition(t) ?: ")
        mode = mode.lower()
        if (mode == 'c'):
            file = ("dracula.caesar.encrypted.txt")
            break
        elif (mode == 't'):
            file = ("dracula.transposition.encrypted.txt")
            break

    inputFile = file

    if not os.path.exists(file):
        print('[*]The file %s does not exist. Quitting...' %(file))
        sys.exit()

    outputFile = os.path.splitext("dracula")[0]
    if(mode == 'c'):
        outputFile=outputFile+'.caesar.decrypted.txt'
    elif (mode == 't'):
        outputFile=outputFile+'.transposition.decrypted.txt'

    file = open(inputFile)
    message = file.read()
    file.close()

    print('processing...' )


    if mode == 'c':
        result = decrypt_caesar(key, message)
    elif mode == 't':
        result = decrypt_transposition(key, message)



    file = open(outputFile, 'w')
    file.write(result)
    file.close()

    print('output file is %s' % (outputFile))

def main():

    while(1):
        mode = input("Encrypt(e) atau Decrypt(d) ?: ")
        mode = mode.lower()
        if (mode == 'e'):
            main_encrypt()
            break
        elif (mode == 'd'):
            main_decrypt()
            break

if __name__ == '__main__':
    main()