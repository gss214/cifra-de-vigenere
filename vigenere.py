import string as s

class Vigenere():
    def __init__(self) -> None:
        self.alphabet = list(s.ascii_uppercase)

    def crypt(self, key, text):
        new_key = self.key_pattern(key, text)
        text_crypt = ""
        for i in range(len(text)):
            text_crypt += self.alphabet[(ord(text[i]) - 65 + ord(new_key[i]) - 65) % 26]
        return text_crypt

    def decrypt(self, key, text):
        new_key = self.key_pattern(key, text)
        text_decrypt = ""
        for i in range(len(text)):
            text_decrypt += self.alphabet[(ord(text[i]) - 65 - ord(new_key[i]) - 65) % 26]
        return text_decrypt

    def key_pattern(self, key, text):
        new_key = ""
        i = 0
        for _ in text:
            new_key += key[i]
            i = i + 1 if i < len(key)-1 else 0
        return new_key

vigenere = Vigenere()

KEY = input()
TEXT = input()

crypt = vigenere.crypt(KEY, TEXT)
decrypt = vigenere.decrypt(KEY, crypt)

print(f'Texto cifrado: {crypt}')
print(f'Texto descriptografado: {decrypt}')
