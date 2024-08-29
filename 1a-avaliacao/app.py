# 1 Cálculo de juros simples. Defina variáveis para o valor inicial, a taxa de juros anual (em
# decimal) e o tempo (em anos). Calcule o valor final de um investimento usando a fórmula
# de juros simples: Valor Final = Valor Inicial * (1 + Taxa * Tempo) . Certifique-se
# de que os valores informados sejam positivos e que a taxa de juros seja decimal (float,
# algo como 0.05 ao ano). Casos todos valores sejam válidos imprima o resultado do juros,
# caso algum valor não atenda os requisitos informe o que está errado.

# Definição da função para cálculo de juros simples
def calcular_juros_simples(valor_inicial, taxa_juros_anual, tempo_anos):
    # Validação dos valores de entrada
    if valor_inicial <= 0:
        return "Erro: O valor inicial deve ser positivo."
    if taxa_juros_anual <= 0 or taxa_juros_anual >= 1:
        return "Erro: A taxa de juros deve ser um número decimal positivo entre 0 e 1 (exemplo: 0.05)."
    if tempo_anos <= 0:
        return "Erro: O tempo deve ser positivo."

    # Cálculo do valor final com juros simples
    valor_final = valor_inicial * (1 + taxa_juros_anual * tempo_anos)
    return f"O valor final do investimento é: R$ {valor_final:.2f}"

# Exemplo de uso
valor_inicial = 1000  # valor inicial do investimento
taxa_juros_anual = 0.05  # taxa de juros anual
tempo_anos = 3  # tempo do investimento em anos

# Chamada da função
resultado = calcular_juros_simples(valor_inicial, taxa_juros_anual, tempo_anos)
print(resultado)




# 2   Receba uma string via input , remova espaços e converta para minúsculas. Verifique se
# a string é um palíndromo (ou seja, se a palavra é a mesma quando lida de trás para
# frente). Exiba uma mensagem indicando se é ou não.



# Função para verificar se uma string é um palíndromo
def verificar_palindromo(string):
    # Remover espaços e converter para minúsculas
    string = string.replace(" ", "").lower()
    
    # Verificar se a string é igual à sua reversa
    if string == string[::-1]:
        return "A string é um palíndromo."
    else:
        return "A string não é um palíndromo."

# Recebendo a string do usuário
entrada = input("Digite uma palavra ou frase: ")

# Chamando a função e exibindo o resultado
resultado = verificar_palindromo(entrada)
print(resultado)



# 3 Dada a frase A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha
# a rã. Nem a rã arranha a aranha. , conte quantas vezes cada palavra aparece.
# Armazene os resultados em um dicionário e exiba-o. Deve fazer um saneamento dos
# dados, considerando apenas palavras/letras, também deve ser considerado maiúsculas e
# minúsculas iguais.


import string

# Função para contar a frequência de palavras em uma frase
def contar_palavras(frase):
    # Converter a frase para minúsculas
    frase = frase.lower()
    
    # Remover pontuações usando string.punctuation
    frase = frase.translate(str.maketrans("", "", string.punctuation))
    
    # Dividir a frase em palavras
    palavras = frase.split()
    
    # Dicionário para armazenar a contagem de palavras
    contagem = {}
    
    # Contar a frequência de cada palavra
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    
    return contagem

# Frase fornecida
frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."

# Chamando a função e exibindo o resultado
resultado = contar_palavras(frase)
print(resultado)



# 4  Dado a lista de idades: [4, 13, 18, 65, 30, 8, 17, 74] . Classifique cada idade em
# 'criança', 'adolescente', 'adulto' ou 'idoso'. Armazene os resultados em um dicionário e
# exiba-o. Onde até 12 anos é criança, entre 13 e 17 adolescente, entre 18 e 64 adulto e
# acima de 64 idoso.


# Função para classificar idades
def classificar_idades(lista_idades):
    classificacao = {}

    for idade in lista_idades:
        if idade <= 12:
            classificacao[idade] = 'criança'
        elif 13 <= idade <= 17:
            classificacao[idade] = 'adolescente'
        elif 18 <= idade <= 64:
            classificacao[idade] = 'adulto'
        else:
            classificacao[idade] = 'idoso'

    return classificacao

# Lista de idades fornecida
idades = [4, 13, 18, 65, 30, 8, 17, 74]

# Chamando a função e exibindo o resultado
resultado = classificar_idades(idades)
print(resultado)


# 5 Receba uma temperatura em Celsius via input e converta para Fahrenheit usando a
# fórmula F = C * 9/5 + 32 . Exiba o resultado.


# Função para converter Celsius para Fahrenheit
def converter_para_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Receber a temperatura em Celsius do usuário
celsius = float(input("Digite a temperatura em Celsius: "))

# Converter para Fahrenheit
fahrenheit = converter_para_fahrenheit(celsius)

# Exibir o resultado
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")



 #6 Dada a string Python é incrível! , conte o número de vogais. Exiba o total.


# Função para contar o número de vogais em uma string
def contar_vogais(string):
    # Definir as vogais
    vogais = "aeiouáéíóúãõâêîôû"
    # Converter a string para minúsculas para garantir a contagem correta
    string = string.lower()
    # Inicializar o contador de vogais
    contador = 0
    
    # Contar as vogais
    for caractere in string:
        if caractere in vogais:
            contador += 1
    
    return contador

# String fornecida
string = "Python é incrível!"

# Chamando a função e exibindo o resultado
total_vogais = contar_vogais(string)
print(f"O total de vogais na string é: {total_vogais}")



# 7) Simule o lançamento de dois dados e exiba a soma dos valores obtidos e o número da
# tentativa a cada iteração. Repita até que a soma dos dados seja igual a 7 ou 11. Mostre
# quantas tentativas foram necessárias para chegar a 7 ou 11 ao final do processo. Para
# gerar o número do dado a cada iteração utilize random.randint(1, 6) , irá gerar um
# número aleatório entre 1 e 6, importe o seguinte pacote import random para utilizar a
# classe random.

import random

tentativas = 0
soma = 0

while soma != 7 and soma != 11:

    dadoA = random.randint(1, 6)
    dadoB = random.randint(1, 6)
    
    soma = dadoA + dadoB
    
    tentativas += 1
    
    print(f"Tentativa {tentativas}: dadoA = {dadoA}, dadoB = {dadoB}, soma = {soma}")

print(f"Foi necessário {tentativas} tentativas para alcançar uma soma de {soma}.")

# 8) Dado o dicionário valores = {"a": 10, "b": 20, "c": 30} , some todos os valores e
# exiba o total.


valores = {"a": 10, "b": 20, "c": 30}
total = sum(valores.values())
print(total)



# 9) Dada a string Python é poderoso! , conte o número de consoantes presentes. Exiba o
# total.

texto = "Python é poderoso!"

consoantes = "bcdfghjklmnpqrstvwxyz"

total_consoantes = sum(1 for char in texto.lower() if char in consoantes)

print(total_consoantes)

# 10)  Dada a lista de salários [1200, 2500, 4000, 7500, 10000] , agrupe-os em 'baixo' (<=
# 2000), 'médio' (2001 - 5000) e 'alto' (> 5000). Armazene os resultados em um dicionário e
# exiba-o.
valores = [1200, 2500, 4000, 7500, 10000]

salarios_agrupados = {"baixo": [], "médio": [], "alto": []}

for salario in valores:
    if salario <= 2000:
        salarios_agrupados["baixo"].append(salario)
    elif 2001 <= salario <= 5000:
        salarios_agrupados["médio"].append(salario)
    else:
        salarios_agrupados["alto"].append(salario)

print(salarios_agrupados)


# 11) Dada a frase frase = "Ana gosta de estudar e aprender novas coisas" , conte
# quantas palavras começam com uma vogal. Exiba o total.

vogais = "aeiou"

frase = "Ana gosta de estudar e aprender novas coisas"

palavras = frase.split()

total_vogais = sum(1 for palavra in palavras if palavra[0].lower() in vogais)

print(total_vogais)

# 12. Dado o dicionário de estudantes e suas notas, classifique cada estudante em uma das
# categorias de A a F, conforme a tabela abaixo:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 50-59
# F: abaixo de 50
# Deve ser impresso a lista das notas classificadas e qual usuário possui essa
# classificação de nota.


estudantes = {
    'Alice': 95,
    'Bob': 82,
    'Charlie': 73,
    'David': 60,
    'Eva': 47,
    'Frank': 55
}

def classificar_nota(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota <= 89:
        return 'B'
    elif 70 <= nota <= 79:
        return 'C'
    elif 60 <= nota <= 69:
        return 'D'
    elif 50 <= nota <= 59:
        return 'E'
    else:
        return 'F'

classificacoes = {estudante: classificar_nota(nota) for estudante, nota in estudantes.items()}

for estudante, classificacao in classificacoes.items():
    print(f"{estudante} obteve uma nota classificada como: {classificacao}")
