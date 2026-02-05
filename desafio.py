# Desafio

# Crie uma função que mostre se os números são pares ou ímpares, começando do 0 até um número máximo indicado como entrada na função.

# Você deve:
# Criar uma função chamada verificar_numeros
# A função deve receber um número inteiro como parâmetro, que representa o valor máximo

# Dentro da função:
# Usar um loop para contar de 0 até o número máximo
# Para cada número, verificar se ele é par ou ímpar

# Dica: Para verificar se um número é par, o resto da divisão do número por 2 é igual a 0 => num % 2 == 0:

# 1 - Definir função, que recebe o número máximo como parâmetro
def verificar_numeros(maximo):
  print(f"O valor {maximo} é o limite")

verificar_numeros(50)

# 2 - Criar estrutura de repetição até o número máximo

def verificar_numeros(maximo):
  for i in range(maximo+1):
    print(i)

verificar_numeros(50)
# 3 - Verificar (if/else) se é par ou não
def verificar_numeros(maximo):
  for i in range(maximo+1):
    if(i % 2 == 0):
      print(f"{i} é par")
    else:  
      print(f"{i} é impar")
      
verificar_numeros(50)