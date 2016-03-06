import sys
from PlayFair import PlayFair

ciphers = {'PLF': 'Playfair', 'RTS': 'Row Transposition', 'RFC': 'Railfence', 'VIG': 'Vigenre', 'CES': 'Carsar',
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

    if not (cipherName in ciphers.keys()):
        print("Valid Ciphers are : ")
        for key, value in ciphers.items():
            print(key, value)

    elif activity == "DEC":
        if not encryption:
            print("You have to encrypt before you can decrypt")

    elif activity == "ENC":
        if cipherName == 'PLF':

            cipher = PlayFair()
            text = fileReader.read()
            fileWriter.write(text)
            fileReader.close()
            fileWriter.close()



