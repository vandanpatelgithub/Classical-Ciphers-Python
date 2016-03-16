import sys
from PlayFair import PlayFair
from RowTransposition import RowTransposition
from Caesar import Caesar
from RailFence import RailFence

ciphers = {'PLF': 'Playfair', 'RTS': 'Row Transposition', 'RFC': 'Railfence', 'VIG': 'Vigenre', 'CES': 'Caesar',
           'MAC': 'Monoalphabetic Cipher'}

activities = {'ENC', 'DEC'}

encryption = False

if len(sys.argv) < 6:

    print("You haven't entered the input correctly!")

    print("Correct Input = python cipher.py <CIPHER NAME> <KEY> <ENC/DEC> <INPUT-FILE> <OUTPUT-FILE>")

else:

    cipherName = sys.argv[1]

    cipherKey = sys.argv[2]

    activity = sys.argv[3]

    inputFile = sys.argv[4]

    outputFile = sys.argv[5]

    fileReader = open(inputFile, 'r')

    fileWriter = open(outputFile, 'w')

    cipherKey = cipherKey.upper()

    if not (cipherName in ciphers.keys()):
        print("Valid Ciphers are : ")
        for key, value in ciphers.items():
            print(key, value)

    elif activity == "ENC":
        if cipherName == 'PLF':
            cipher = PlayFair()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            cipherText = cipher.encrypt(text)
            fileWriter.write(cipherText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'RTS':
            cipher = RowTransposition()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            cipherText = cipher.encrypt(text)
            fileWriter.write(cipherText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'CES':
            cipher = Caesar()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            cipherText = cipher.encrypt(text)
            fileWriter.write(cipherText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'RFC':
            cipher = RailFence()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            cipherText = cipher.encrypt(text)
            fileWriter.write(cipherText)
            fileReader.close()
            fileWriter.close()

    elif activity == "DEC":
        if cipherName == "PLF":
            cipher = PlayFair()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            plainText = cipher.decrypt(text)
            fileWriter.write(plainText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'RTS':
            cipher = RowTransposition()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            plainText = cipher.decrypt(text)
            fileWriter.write(plainText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'CES':
            cipher = Caesar()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            plainText = cipher.decrypt(text)
            fileWriter.write(plainText)
            fileReader.close()
            fileWriter.close()

        if cipherName == 'RFC':
            cipher = RailFence()
            cipher.setKey(cipherKey)
            text = fileReader.read()
            plainText = cipher.decrypt(text)
            fileWriter.write(plainText)
            fileReader.close()
            fileWriter.close()
