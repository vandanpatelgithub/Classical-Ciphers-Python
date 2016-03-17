import CipherInterface

import re

import sys

class Vigenre(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""

    def __init__(self):
        print("You are using Vigenre")

    def setKey(self, key):
        self.key = key

    def prepareKeyText(self, plaintext):

        counter = 0

        plaintext_length = len(plaintext)

        print("Plaintext length : " + str(plaintext_length))

        key_length = int(len(self.key))

        print("Key Length : " + str(key_length))

        if key_length < plaintext_length:

            repeatitions = plaintext_length / key_length

            remainder = plaintext_length % key_length

            self.key *= repeatitions

            while remainder > 0:
                self.key += self.key[counter]
                counter += 1
                remainder -= 1

        else:

            newcounter = 0

            newkey = ""

            while newcounter < plaintext_length:
                newkey += self.key[newcounter]
                newcounter += 1

            self.key = newkey

        return self.key

    def encrypt(self, plainText):

        keyindex_list = []

        plaintextindex_list = []

        cipherindex_list = []

        alpabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.plaintext = self.prepareText(plainText)

        self.key = self.prepareKeyText(self.plaintext)

        print(self.key)

        for e in range(int(len(self.key))):
            cipherindex_list.append('')

        for key in self.key:
            keyindex_list.append(alpabetic.index(key))

        for text in self.plaintext:
            plaintextindex_list.append(alpabetic.index(text))

        cipherindex_list = [(a+b)%26 for a,b in zip(keyindex_list, plaintextindex_list)]

        for index in cipherindex_list:
            self.ciphertext += alpabetic[index]
        print(self.ciphertext)

        return self.ciphertext

    def decrypt(self, cipherText):

        keyindex_list = []

        ciphertextindex_list = []

        plaintextindex_list = []

        alphabetic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.ciphertext = cipherText

        self.key = self.prepareKeyText(self.ciphertext)

        print("Key is : " + self.key)

        for e in range(int(len(self.key))):
            plaintextindex_list.append('')

        for key in self.key:
            keyindex_list.append(alphabetic.index(key))

        for text in self.ciphertext:
            ciphertextindex_list.append(alphabetic.index(text))

        plaintextindex_list = [(a-b)%26 for a,b in zip(ciphertextindex_list, keyindex_list)]

        for index in plaintextindex_list:
            if index < 0:
                index += 26
            self.plaintext += alphabetic[index]

        return self.plaintext

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext