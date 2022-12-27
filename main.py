from vigenere import Vigenere

def read_file():
    filename = input('Digite o nome do arquivo que esta contida a mensagem (o arquivo tem que esta na pasta tests/ArquivosDeTestes).\n>>> ')
    try:
        with open(f'tests/ArquivosDeTestes/{filename}', encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f'ERRO: O arquivo {filename} nao existe')
        return None

def menu():
    print('------------------')
    print('Escolha uma opcao:')
    print('\t1 - Cifrar')
    print('\t2 - Decifrar')
    print('\t3 - Ataque')
    print('\t4 - Sair')
    print('------------------')
    op = input(">>> ")
    return op

vigenere = Vigenere()

while True:
    option = menu()

    if option == '1':
        message = read_file()
        if message:
            key = input('Digite a chave para cifrar a mensagem.\n>>> ')
            message_crypt = vigenere.crypt_decrypt(key, message, 'C')
            print("Mensagem cifrada:")
            print(message_crypt)
    elif option == '2':
        message = read_file()
        if message:
            key = input('Digite a chave para descifrar a mensagem.\n>>> ')
            message_decrypt = vigenere.crypt_decrypt(key, message, 'D')
            print("Mensagem descifrada:")
            print(message_decrypt)
    elif option == '3':
        mensagem = read_file()
        if mensagem:
            language = input("A mensagem esta em portugues ou ingles (PT/EN)?\n>>> ")
            end = False

            while not end:
                key_size = vigenere.key_size(mensagem)
                keyword = vigenere.break_keyword(key_size, mensagem.upper(), language)

                print("Palavra-chave obtida: ", keyword)
                print("Mensagem decriptografada:")
                print(vigenere.crypt_decrypt(keyword, mensagem, 'D'))

                ans = input("Deseja refazer o ataque com outro tamanho de chave (S/N)?\n>>> ")
                end = (True if ans.upper() == 'N' else False)
    elif option == '4':
        break
    else:
        print("Opcao inválida")
