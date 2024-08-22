# 7) Simule o lançamento de dois dados e exiba a soma dos valores obtidos e o número da
# tentativa a cada iteração. Repita até que a soma dos dados seja igual a 7 ou 11. Mostre
# quantas tentativas foram necessárias para chegar a 7 ou 11 ao final do processo. Para
# gerar o número do dado a cada iteração utilize random.randint(1, 6) , irá gerar um
# número aleatório entre 1 e 6, importe o seguinte pacote import random para utilizar a
# classe random.


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
