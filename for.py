# percorrer lista de vendas e adicionar em outra lista
# vendas = [10, 20, 30]
# lista = []
# for item in vendas:
#     lista.append(item * 0.3)
#     print(f"{item:.2f}")

# executar codigo for em uma quantidade definida de vezes
# for i in range():


# EXERCICIOS

# qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
# quarto = []

# for i in range(qtde_pessoas):
#     nome = input('Qual o nome?')
#     cpf = input('Qual o cpf?')
#     hospede = [nome, 'cpf:{}'.format(cpf)]
#     quarto.append(hospede)
    
# print(quarto)


# EXERCICIO 2

# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]

# for item in vendas:
#     if item[1] >= meta:
#         print(f'{item[0]} bateu a meta com {item[1]} vendas')


# EXERCICIO 3

# produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
# vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
# vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

# result = []

# for i, item in enumerate(produtos):
#     if vendas2020[i] > vendas2019[i]:
#         crescimento = (vendas2020[i]/vendas2019[i]) - 1
#         print('O valor das vendas de 2019 foi {}, de 2020 foi {}, com crescimento de {:.2%}'.format(vendas2019[i],vendas2020[i], crescimento))
       
# def convert(lista):
#     keys = lista[::2]  
#     values = lista[1::2] 
#     dict = {keys[i]: values[i] for i in range(len(keys))}
#     return dict
# print(convert(result))
