import unittest
from vigenere import Vigenere

class TestVigenere(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.vigenere = Vigenere()
        self.challenges_crypt = ['desafio1.txt', 'desafio2.txt']
        self.challenges_decrypt = ['desafio1_d.txt', 'desafio2_d.txt']
        self.filenames = ['001.txt', '002.txt', '003.txt', '004.txt', '005.txt', '006.txt', '007.txt']
        self.messages_crypt = ['001_c.txt', '002_c.txt', '003_c.txt', '004_c.txt', '005_c.txt', '006_c.txt', '007_c.txt']
        self.keys = ['GUI', 'TIMMAIA', 'DUDA', 'QUEEN', 'GUIDUDA', 'AMBRIOSETHOMAS', 'LEMON']
    
    def read_file(self, filename):
        try:
            with open(f'tests/ArquivosDeTestes/{filename}', encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f'ERRO: O arquivo {filename} nao existe')
            return None

    def test_crypt(self):
        for i, file in enumerate(self.filenames):
            message = self.read_file(file)
            message_crypt = self.read_file(self.messages_crypt[i]).upper()
            key = self.keys[i]
            self.assertEqual(self.vigenere.crypt_decrypt(key, message, 'C'), message_crypt)

    def test_decrypt(self):
        for i, file in enumerate(self.messages_crypt):
            message = self.read_file(file)
            message_decrypt = self.read_file(self.filenames[i]).upper()
            key = self.keys[i]
            self.assertEqual(self.vigenere.crypt_decrypt(key, message, 'D'), message_decrypt)

    def test_attack(self):
        keys = ['ARARA', 'TEMPORAL']
        langs = ['PT', 'EN']
        keys_size = [5,8]

        for i, file in enumerate(self.challenges_crypt):
            message_crypt = self.read_file(file)
            message_decrypt = self.read_file(self.challenges_decrypt[i]).upper()
            keyword = self.vigenere.break_keyword(keys_size[i], message_crypt.upper(), langs[i])
            self.assertEqual(keyword, keys[i])
            self.assertEqual(self.vigenere.crypt_decrypt(keyword, message_crypt, 'D'), message_decrypt)
        
if __name__ == '__name__':
    unittest.main()
