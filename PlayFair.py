import CipherInterface

import re


class PlayFair(CipherInterface.CipherInterface):
    key = ""
    plaintext = ""
    ciphertext = ""
    row = ""
    column = ""
    diagraphs = []

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

    def buildDiagraph(self, plaintext):

        counter = 0

        while counter < len(plaintext):

            if counter + 1 == len(plaintext):
                diagraph = plaintext[counter] + "X"
                self.diagraphs.append(diagraph)
                break

            elif plaintext[counter] != plaintext[counter + 1]:
                diagraph = plaintext[counter] + plaintext[counter + 1]
                self.diagraphs.append(diagraph)
                counter += 2

            else:
                diagraph = plaintext[counter] + "X"
                self.diagraphs.append(diagraph)
                counter += 1

        return self.diagraphs

    def buildIndexArray(self, keyMatrix):

        indices = []

        for e in range(26):
            indices.append('')

        row = 0
        column = 0

        for key in keyMatrix:
            for value in key:
                indices[ord(str(value))-65] = ((row%5), (column%5))
                column += 1
            row += 1

        return indices

    def prepareText(self, text):

        text = text.upper()

        text = text.replace("J", "I")

        text = re.sub(r'\W+', '', text)

        return text

    def encrypt(self, plaintext):

        self.plaintext = self.prepareText(plaintext)

        diagraphs = self.buildDiagraph(self.plaintext)

        keyMatrix = self.setKey(self.key)

        print(keyMatrix)

        indices = self.buildIndexArray(keyMatrix)

        for pair in diagraphs:

            firstelementindex = ord(str(pair[0])) - 65
            secondelementindex = ord(str(pair[1])) - 65

            firstelement = indices[firstelementindex]
            secondelement = indices[secondelementindex]

            zipped = firstelement + secondelement

            if(zipped[0] == zipped[2]):
                row = zipped[0]
                newcolumn_firstelement = (zipped[1] + 1) % 5
                newcolumn_secondelement = (zipped[3] + 1) % 5

                encrypted_first_element = keyMatrix[row][newcolumn_firstelement]
                encrypted_second_element = keyMatrix[row][newcolumn_secondelement]

                print("They are in the same row")
                print("Encrypted Output : " + encrypted_first_element + encrypted_second_element)
                self.ciphertext += encrypted_first_element + encrypted_second_element

            elif(zipped[1] == zipped[3]):
                column = zipped[1]
                newrow_firstelement = (zipped[0] + 1) % 5
                newrow_secondelement = (zipped[2] + 1) % 5

                encrypted_first_element = keyMatrix[newrow_firstelement][column]
                encrypted_second_element = keyMatrix[newrow_secondelement][column]

                print("They are in the same columns!")
                print("Encrypted Output : " + encrypted_first_element + encrypted_second_element)
                self.ciphertext += encrypted_first_element + encrypted_second_element

            else:
                encrypted_first_element = keyMatrix[zipped[0]][zipped[3]]
                encrypted_second_element = keyMatrix[zipped[2]][zipped[1]]
                print("They are not in same rows or columns!")
                print("Encrypted Output : " + encrypted_first_element + encrypted_second_element)
                self.ciphertext += encrypted_first_element + encrypted_second_element

        return self.ciphertext

    def decrypt(self, ciphertext):

        self.ciphertext = self.prepareText(ciphertext)

        diagraphs = self.buildDiagraph(self.ciphertext)

        keyMatrix = self.setKey(self.key)

        print(keyMatrix)

        indices = self.buildIndexArray(keyMatrix)

        for pair in diagraphs:

            firstelementindex = ord(str(pair[0])) - 65
            secondelementindex = ord(str(pair[1])) - 65

            firstelement = indices[firstelementindex]
            secondelement = indices[secondelementindex]

            zipped = firstelement + secondelement

            if(zipped[0] == zipped[2]):

                row = zipped[0]
                newcolumn_firstelement = (zipped[1] - 1)
                newcolumn_secondelement = (zipped[3] - 1)

                if newcolumn_firstelement < 0:
                    newcolumn_firstelement += 5

                if newcolumn_secondelement < 0:
                    newcolumn_secondelement += 5

                decrypted_first_element = keyMatrix[row][newcolumn_firstelement]
                decrypted_second_element = keyMatrix[row][newcolumn_secondelement]

                print("Decrypted Output : " + decrypted_first_element + decrypted_second_element)
                self.plaintext += decrypted_first_element + decrypted_second_element

            elif(zipped[1] == zipped[3]):

                column = zipped[1]
                newrow_firstelement = (zipped[0] - 1)
                newrow_secondelement = (zipped[2] - 1)

                if newrow_firstelement < 0:
                    newrow_firstelement += 5

                if newrow_secondelement < 0:
                    newrow_secondelement += 5

                decrypted_first_element = keyMatrix[newrow_firstelement][column]
                decrypted_second_element = keyMatrix[newrow_secondelement][column]

                print("Decrypted Output : " + decrypted_first_element + decrypted_second_element)
                self.plaintext += decrypted_first_element + decrypted_second_element

            else:

                encrypted_first_element = keyMatrix[zipped[0]][zipped[3]]
                encrypted_second_element = keyMatrix[zipped[2]][zipped[1]]
                print("They are not in same rows or columns!")
                print("Encrypted Output : " + encrypted_first_element + encrypted_second_element)
                self.plaintext += encrypted_first_element + encrypted_second_element

        return self.plaintext

