import time, os, sys

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def encryptt(key, message):
    global SYMBOLS
    translated= ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol


    return translated

def decryptt(key, message):
    global SYMBOLS
    translated= ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol


    return translated

def main():

    key = 10


    while(1):
        mode = input("encrypt(e) atau decrypt(d) ?: ")
        mode = mode.lower()
        if (mode == 'e'):
            break
        elif (mode == 'd'):
            break

    while(1):
        file = input("nama file: ")
        inputFilename = file
        if not os.path.exists(inputFilename):
            print('The file %s does not exist.' )
        else:
            break
        

    inputFile = file

    outputFile = os.path.splitext(file)[0]
    if(mode == 'e'):
        outputFile=outputFile+'.encrypted.txt'
    elif (mode == 'd'):
        outputFile=outputFile+'.decrypted.txt'

    file = open(inputFile)
    message = file.read()
    file.close()

    print('processing...' )

    startTime = time.time()
    if mode == 'e':
        translated = encryptt(key, message)
    elif mode == 'd':
        translated = decryptt(key, message)
    totalTime = round(time.time() - startTime, 2)
    print('processing time: %s seconds' % (totalTime))

    # Write out the translated message to the output file:
    file = open(outputFile, 'w')
    file.write(translated)
    file.close()

    # print('Done %sing %s (%s characters).' % (Mode, inputFilename, len(message)))
    print('output file is %s.' % (outputFile))


if __name__ == '__main__':
    main()