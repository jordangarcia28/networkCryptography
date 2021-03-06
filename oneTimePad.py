import secrets

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def generateOtp(message):
    otp = ''
    for i in range(len(message)):
        otp += secrets.choice(LETTERS)
    return otp.upper()

def main():
    myMessage = "\"Encryption works. Properly implemented strong crypto systems are one of the few things that you can rely on. Unfortunately, endpoint security is so terrifically weak that NSA can frequently find ways around it.\" ― Edward Snowden"
    myKey = generateOtp(myMessage)

    translatedEncrypt = encryptMessage(myKey, myMessage)
    translatedDecrypt = decryptMessage(myKey, translatedEncrypt)

    print('One Time Pad Key:')
    print(myKey)
    print('\nOne Time Pad ciphertext:')
    print(translatedEncrypt)
    print('\nOne Time Pad plaintext:')
    print(translatedDecrypt)


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] 

    keyIndex = 0
    key = key

    for symbol in message: 
        num = LETTERS.find(symbol)
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) 
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) 

            num %= len(LETTERS) 

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)

if __name__ == '__main__':
    main()