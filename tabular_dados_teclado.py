import time
from tabulate import tabulate

def tfunction(texto):
	for palavra in texto:
		print(palavra, end='', flush= True)
		time.sleep(0.1)


tfunction('Esse programa tabula os resultados que são inseridos \n')



N = input("Digite o numero de pessoas: \n")
N = int(N)

table     = [];
names     = [];
LastNames = [];
ages      = [];

for i in range(N):
	name = input("Digite o nome: \n")
	names.append(name)
	LastName = input("Digite o sobrenome: \n")
	LastNames.append(LastName)
	age = input("Digite a idade: \n")
	ages.append(age)

cab = ['First Name', 'Last Name', 'Age']
table = {cab[0]: names, cab[1]: LastNames, cab[2]: ages}


tfunction('Seus dados organizados ...\n')
print(tabulate(table, headers='keys',tablefmt='fancy_grid'))

tfunction('O código simples do LaTex com os dados inseridos...\n')
print(tabulate(table, headers='keys',tablefmt='latex'))

