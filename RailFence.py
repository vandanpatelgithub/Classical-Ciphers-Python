import CipherInterface

import re

import sys


class RailFence(CipherInterface.CipherInterface):

    key = ""
    plaintext = ""
    ciphertext = ""
    start, end = 0, 0
    isKey = True

    def __init__(self):
        print("You are using RailFence")

    def setKey(self, key):

        if not self.RepresentsInt(key):
            print("Key Has To Be Integer")
            self.isKey = False
            sys.exit()
        elif int(key) < 0:
            print("Key Has to Be Positive Integer")
            self.isKey = False
            sys.exit()

        self.key = key

        return self.isKey

    def encrypt(self, plainText):

        if self.isKey:

            self.plaintext = self.prepareText(plainText)

            depth = int(self.key)

            depth_list = [self.plaintext[i:i+depth] for i in range(0, len(self.plaintext), depth)]

            depth_counter = 0

            while depth_counter < depth:
                for lists in depth_list:
                        length = len(lists)
                        if depth_counter < length:
                            self.ciphertext += lists[depth_counter]
                depth_counter += 1

            return self.ciphertext

        else:

            print("Something is wrong with the key!")
            sys.exit()

    def decrypt(self, cipherText):

        if self.isKey:

            counter, length_counter = 0, 0

            ciphertext_list = []

            self.ciphertext = cipherText

            ciphertext_length = len(self.ciphertext)

            depth = int(self.key)

            rows = ciphertext_length / depth

            remaining_letters = ciphertext_length % depth

            while counter < depth:

                if remaining_letters > 0:
                    self.end += rows + 1
                    ciphertext_list.append(self.ciphertext[self.start:self.end])
                    remaining_letters -= 1
                    self.start = self.end
                    counter += 1
                else:
                    self.end += rows
                    ciphertext_list.append(self.ciphertext[self.start:self.end])
                    self.start = self.end
                    counter += 1

            max_length = len(ciphertext_list[0])

            while length_counter < max_length:
                for lists in ciphertext_list:
                    length = len(lists)
                    if length_counter < length:
                        self.plaintext += lists[length_counter]
                length_counter += 1

            return self.plaintext

        else:

            print("Something is wrong with the key!")
            sys.exit()

    def prepareText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        return plaintext

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
