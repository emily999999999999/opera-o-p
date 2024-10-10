numero1 = float (input("Digite um numero"))
numero2 = float (input("Digite outro numero"))
operação = input ("Digite a operação,+,-,/,*")

soma= numero1 + numero2
subtraçao= numero1 - numero2
divisao= numero1 / numero2
multiplicação= numero1 * numero2

print("Soma:", soma)
print("Subtraçao:", subtracao)
print("Divisao:", divisao)
print("Multiplicação:", multiplicacao)

resultado = calcular (operacao, numero1, numero2)
print("Resultado :", resultado)