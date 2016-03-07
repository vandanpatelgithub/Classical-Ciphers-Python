import CipherInterface

import re


class PlayFair(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    row = ""
    column = ""

    def __init__(self):
        print('You are using PlayFair')

    def setKey(self, key):
        self.key = key

        keyList = []
        keyMatrix = []

        for k in key:
            if k not in keyList:
                keyList.append(k)

        alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for alphabet in alphabets:
            if alphabet not in keyList:
                keyList.append(alphabet)

        for e in range(5):
            keyMatrix.append('')

        keyMatrix[0] = keyList[0:5]
        keyMatrix[1] = keyList[5:10]
        keyMatrix[2] = keyList[10:15]
        keyMatrix[3] = keyList[15:20]
        keyMatrix[4] = keyList[20:25]

        return keyMatrix

    def encrypt(self, plaintext):

        self.plaintext = plaintext

        diagraphs = []

        keyMatrix = self.setKey(self.key)

        plaintext = re.sub(r'\W+', '', plaintext)

        plaintext = plaintext.upper()

        print("Your plaintext is : " + plaintext)

        counter = 0

        while counter < len(plaintext):

            if counter + 1 == len(plaintext):
                diagraph = plaintext[counter] + "X"
                diagraphs.append(diagraph)
                break

            elif plaintext[counter] != plaintext[counter+1]:
                diagraph = plaintext[counter] + plaintext[counter+1]
                diagraphs.append(diagraph)
                counter += 2

            else:
                diagraph = plaintext[counter] + "X"
                diagraphs.append(diagraph)
                counter += 1

        print("Your input to cipher is : " + str(diagraphs))

        for pair in diagraphs:
            pass

        return self.ciphertext

    def decrypt(self, ciphertext):
        self.ciphertext = ciphertext
        return self.plaintext

    def rowColumn(self, element):
        for i in range(len(self.plaintext)):
            for j in range(len(self.plaintext[i])):
                if self.plaintext[i][j] == element:
                    self.row = j
                    self.column = i
                    break
        return