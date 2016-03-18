import CipherInterface

import re

import sys


class RowTransposition(CipherInterface.CipherInterface):
    key = ""
    plaintext = ""
    ciphertext = ""
    isKey = True

    def __init__(self):
        print("You are using Row Transposition")

    def setKey(self, key):
        newkey = key.split(' ')

        for key in newkey:
            if not self.RepresentsInt(key):
                print('"' + key + '"' + " IS NOT A VALID KEY")
                print("KEY HAS TO BE A INTEGER AND ENTERED AS LIST OF STRING. KEY = 1 2 3 SHOULD BE ENTERED AS '1 2 3'")
                self.isKey = False
                sys.exit()

            elif int(key) < 0:
                print('"' + key + '"' + " IS NOT A VALID KEY")
                print("KEY HAS TO BE POSITIVE VALUE")
                sys.exit()

        newkey = map(int, newkey)
        self.key = newkey

        return self.isKey

    def encrypt(self, plaintext):

        if self.isKey:

            self.plaintext = plaintext

            prepared_text = self.prepateText(self.plaintext)

            key_length = len(self.key)

            length_prepared_text = len(prepared_text)

            for keys in self.key:
                index = keys - 1
                while index < length_prepared_text:
                    self.ciphertext += prepared_text[index]
                    index += key_length

            return self.ciphertext

        else:

            print("Something is wrong with the key !")
            sys.exit()

    def decrypt(self, ciphertext):

        if self.isKey:

            self.ciphertext = self.prepateText(ciphertext)

            ciphertext_length = len(self.ciphertext)

            print(ciphertext_length)

            key_length = len(self.key)

            print(key_length)

            rows = ciphertext_length / key_length

            print(rows)

            ciphertext_list = [self.ciphertext[i:i + rows] for i in range(0, len(self.ciphertext), rows)]

            print(ciphertext_list)

            plaintext_list = []

            counter = 0

            for e in range(len(ciphertext_list)):
                plaintext_list.append('')

            for keys in self.key:
                index = keys - 1
                plaintext_list[index] = ciphertext_list[counter]
                counter += 1

            row_counter = 0

            while row_counter < rows:
                for lists in plaintext_list:
                    self.plaintext += lists[row_counter]
                row_counter += 1

            print("Plaintext is : " + self.plaintext)

            return self.plaintext

        else:

            print("Something is wrong with the key !")
            sys.exit()

    def prepateText(self, plaintext):

        plaintext = plaintext.upper()

        plaintext = re.sub(r'\W+', '', plaintext)

        maxValue = len(self.key)

        text_length = len(plaintext)

        if text_length % maxValue != 0:
            padding_length = maxValue - (text_length % maxValue)

            for e in range(padding_length):
                plaintext += 'X'

        return plaintext

    def RepresentsInt(self, s):

        try:
            int(s)
            return True
        except ValueError:
            return False
