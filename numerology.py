print("Programa para saber qual é o seu número da sorte, equivalente às letras de seu nome.")

nome = str(input("Insira seu nome, somente letras (sem acentos) e espaços:"))

print("Seu nome é " + nome + ".")

nome_low = nome.lower()

sum = 0

for word in nome_low:
    if word == "a" or "j" or "s":
        sum = sum + 1
    elif word == "b" or "K" or "k" or "T" or "t":
        sum = sum + 2
    elif word == "c" or "ç" or "l" or "u":
        sum = sum + 3
    elif word == "d" or "m" or "v":
        sum = sum + 4
    elif word == "e" or "n" or "w":
        sum = sum + 5
    elif word == "f" or "o" or "x":
        sum = sum + 6
    elif word == "g" or "p" or "y":
        sum = sum + 7
    elif word == "h" or "q" or "z":
        sum = sum + 8
    elif word == "i" or "r":
        sum = sum + 9
    elif word == " ":
        sum = sum + 0

final_sum = 0

for word2 in str(sum):
    int_word2 = int(word2)
    final_sum = final_sum + int_word2

print("Seu número da sorte é " + str(final_sum) + ".")
