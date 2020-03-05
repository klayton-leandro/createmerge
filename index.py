#KLAYTON LEANDRO 

#RA 1800060

#Definição de número primos
#Todo número que só tem 2 divisores, o 1 ele mesmo
#Exemplos: 1, 2, 3, 5, 7, 11, .....



n = int(input('[digite um numero]:'))
divisor = 0
i = 1
while i <= n:
	if(n%i) == 0:
		divisor +=1
	i +=1
if divisor ==2:
	print("%d é  primo" %n)
else:
	print("%d não é primo" %n)







