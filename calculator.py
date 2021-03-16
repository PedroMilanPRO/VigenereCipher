abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def criptografar(frase, chave):
    crip_final = ''

    i = 0
    for letra in frase:
        if letra != ' ':
            sum_ = abc.find(letra) + abc.find(chave[i % len(chave)])
            modulo = int(sum_) % len(abc)
            crip_final += str(abc[modulo])
            i += 1
        
    print(f'O texto criptografado é: {crip_final}')

def descriptografar(frase, chave):
    crip_final = ''

    i = 0
    for letra in frase:
        if letra != ' ':
            sub = abc.find(letra) - abc.find(chave[i % len(chave)])
            modulo = int(sub) % len(abc)
            crip_final += str(abc[modulo])
            i += 1
        
    print(f'O texto criptografado é: {crip_final}')


def start():
    frase = input('Frase: ').upper()
    chave = input('Chave: ').upper()
    mode = input('Digite C para Criptografar ou D para descriptografar: ').upper()

    if mode == 'C':
        criptografar(frase, chave)
    if mode == 'D':
        descriptografar(frase, chave)
        

if __name__ == '__main__':
    start()