from vigenere import Vigenere

def readFile():
    nome_arquivo = input('Digite o nome do arquivo que esta contida a mensagem (o arquivo tem que esta na pasta ArquivosDeTestes).\n>>> ')
    lines = []
    try:
        with open(f'ArquivosDeTestes/{nome_arquivo}', encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('ERRO: O arquivo nao existe')
        return None

    output = ""
    for s in lines:
        output += s

    return output
    
vigenere = Vigenere()
op = '0' 

while (op != '4'):

    print('------------------')
    print('Escolha uma opcao:')
    print('\t1 - Cifrar')
    print('\t2 - Decifrar')
    print('\t3 - Ataque')
    print('\t4 - Sair')
    print('------------------')
    op = input(">>> ")

    if op == '1':
        mensagem = readFile()
        if mensagem:
            chave = input('Digite a chave para cifrar a mensagem.\n>>> ')
            mensagem_cifrada = vigenere.crypt_decrypt(chave, mensagem, 'C')
            print("Mensagem cifrada:")
            print(mensagem_cifrada)
    elif op == '2':
        mensagem = readFile()
        if mensagem:
            chave = input('Digite a chave para descifrar a mensagem.\n>>> ')
            mensagem_cifrada = vigenere.crypt_decrypt(chave, mensagem, 'D')
            print("Mensagem descifrada:")
            print(mensagem_cifrada)

    elif op == '3':
        mensagem = readFile()
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
