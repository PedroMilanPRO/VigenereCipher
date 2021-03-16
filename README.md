# Vigenere_cipher_calculator
##### Vigenere Principles:

- Encrypt a text
         - Have a sentence (Password), repeat it until it has the same length as the sentence to be encrypted
         - Iterate each letter of the phrase and password, the first letter of the phrase, with the first letter of the password, and so successively
         -locate horizontally and vertically in the table, and find the number where the two letters meet

- Decrypt a text
         - have the encrypted text (password), find the letter of the password, and go to the letter of the sentence, and go up
         
![](320px-Vigenère_square_shading.svg.png)
##### Example:

- Text: testing 
- Key:  keykeyk
- Cipher text: DIQDMLQ

---
##### Inserting the code...

```python
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
```
---
Inspirations:
- https://youtu.be/XT6zIHXhFO4
- https://youtu.be/rIjLR3OYpCo


If something is wrong, let me know so I can fix it, I am always willing to improve.

![](Hello_Bye.gif)