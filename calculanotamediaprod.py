titulo = "Calcula o valor médio de avaliação do produto"
print(f'{titulo:^50}')

nota1 = int(input("Digite a primeira nota avaliada do produto pelo cliente: "))

nota2 = int(input("Digite a segunda nota avaliada do produto pelo cliente: "))

media = (float(nota1) + float(nota2))/2

print("A média alcançada foi: %s" % media)

if media > 6:
    print("Parabéns, produto adequado aos clientes!")
else:
    print("Que pena, esse produto inadequado e com muitas reclamações!") 
	
		   