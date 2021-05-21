str1, str2, numero = input().split()
numero = numero
numeric_filter = filter(str.isdigit, numero)
numeric_string = int("".join(numeric_filter))
def concatenar(str1, str2):
    return str1 + str2
    
def repetir(str1, str2):
    return str1*numeric_string
    
def ambos(str1, str2):
    return (str1 +str2)*numeric_string

print(concatenar(str1, str2))
print(repetir(str1, str2))
print(ambos(str1, str2))
