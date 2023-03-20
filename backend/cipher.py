def encrypt(inputText, N, D):

    reversedInput = inputText[::-1]
    encryptedText = ""

    if (D == 1):
        for i in range(0, len(inputText)):

            if ord(reversedInput[i]) < 34 or ord(reversedInput[i]) > 126:
                return inputText + " is an invalid input"

            if ((ord(reversedInput[i]) + N) > 126):
                newASCII = ((ord(reversedInput[i]) + N) % 126) + 34 - 1
                encryptedText += chr(newASCII)

            else:
                newASCII = ord(reversedInput[i]) + N
                encryptedText += chr(newASCII)

    elif (D == -1):
        for i in range(0, len(inputText)):
            if ((ord(reversedInput[i]) - N) < 34):
                newASCII = 126 - (34 % (ord(reversedInput[i]) - N)) + 1
                encryptedText += chr(newASCII)

            else:
                newASCII = ord(reversedInput[i]) - N
                encryptedText += chr(newASCII)

    return encryptedText


def decrypt(inputText, N, D):

    reversedInput = inputText[::-1]
    decryptedText = ""

    if (D == 1):

        for i in range(0, len(inputText)):

            if ord(reversedInput[i]) < 34 or ord(reversedInput[i]) > 126:
                return inputText + " is an invalid input"

            if ((ord(reversedInput[i]) - N) < 34):
                newASCII = 126 - (34 % (ord(reversedInput[i]) - N)) + 1
                decryptedText += chr(newASCII)

            else:
                newASCII = ord(reversedInput[i]) - N
                decryptedText += chr(newASCII)

    elif (D == -1):
        for i in range(0, len(inputText)):

            if ((ord(reversedInput[i]) + N) > 126):
                newASCII = ((ord(reversedInput[i]) + N) % 126) + 34 - 1
                decryptedText += chr(newASCII)

            else:
                newASCII = ord(reversedInput[i]) + N
                decryptedText += chr(newASCII)

    return decryptedText