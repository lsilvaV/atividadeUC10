import this
import modelExercicios

opcao = 0

#exercício 2, 7, 14, 16 instanciando variáveis
valor = 0

#exercício 3 instanciando variáveis
base = 0
altura = 0

#exercício 4 instanciando variáveis
ano = 0
mes = 0
dia = 0

#exercicio 5 instanciando variáveis
elei = 0
bran = 0
nulo = 0
vali = 0

#exercicio 8 instanciando variáveis
aluno = ""
nota1 = 0
nota2 = 0
nota3 = 0

#exercicio 8 instanciando variáveis
maca = 0

#exercicio 11 instanciando variáveis
fixo = 0
venda = 0

#exercicio 12 instanciando variáveis
nConta = 0
saldo = 0
debito = 0
credito = 0

#exercicio 13 instanciando variáveis
tabuada = 0

def menu():
    print('Escolha uma das opções abaixo:\n'
          '1. Exercício 1\n'
          '2. Exercício 2\n'
          '3. Exercício 3\n'
          '4. Exercício 4\n'
          '5. Exercício 5\n'
          '6. Exercício 6\n'
          '7. Exercício 7\n'
          '8. Exercício 8\n'
          '9. Exercício 9\n'
          '10. Exercício 10\n'
          '11. Exercício 11\n'
          '12. Exercício 12\n'
          '13. Exercício 13\n'
          '14. Exercício 14\n'
          '15. Exercício 15\n'
          '16. Exercício 16\n'
          '17. Exercício 17\n'
          '18. Exercício 18\n'
          '')
    this.opcao = int(input())

#input exercício 2
def inputExer2():
    print('Informe o número:')
    this.valor = float(input())

#input exercício 3
def inputExer3():
    print('Informe a base do retângulo')
    this.base = float(input())
    print('Informe a altura do retângulo')
    this.altura = float(input())

#input exercício 4
def inputExer4():
    print('Informe o ano em que você nasceu:')
    this.ano = float(input())
    print('Informe o mês (em número) que você nasceu:')
    this.mes = float(input())
    print('Informe o dia em que você nasceu:')
    this.dia = float(input())

#input exercício 5
def inputExer5():
    print('Informe a quantidade de eleitores no município:')
    this.elei = float(input())
    print('Informe o número de votos brancos:')
    this.bran = float(input())
    print('Informe o número de votos nulos:')
    this.nulo = float(input())
    print('Informe o número de votos válidos:')
    this.vali = float(input())

#input exercício 6
def inputExer6():
    print('Informe o salário:')
    this.sala = float(input())
    print('Informe o percentual de reajuste:')
    this.reaj = float(input())

#input exercício 7
def inputExer7():
    print('Informe o valor de fábrica:')
    this.valor = float(input())

#input exercício 8
def inputExer8():
    print('Informe o nome do aluno:')
    this.aluno = str(input())
    print('Informe a primeira nota do aluno:')
    this.nota1 = float(input())
    print('Informe a segunda nota do aluno:')
    this.nota2 = float(input())
    print('Informe a terceira nota do aluno:')
    this.nota3 = float(input())

#input exercício 9
def inputExer9():
    print('Informe a quantidade de maçãs:')
    this.maca = float(input())

#input exercício 11
def inputExer11():
    print('Informe o salário fixo:')
    this.fixo = float(input())
    print('Informe o valor das vendas')
    this.venda = float(input())

#input exercício 12
def inputExer12():
    print('Informe o número da conta:')
    this.nConta = float(input())
    print('Informe o saldo da conta:')
    this.saldo = float(input())
    print('Informe o débito:')
    this.debito = float(input())
    print('Informe o crédito:')
    this.credito = float(input())

#input exercício 13
def inputExer13():
    print('Informe o número para montar uma tabuada:')
    this.tabuada = float(input())

#input exercício 14
def inputExer14():
    print('Informe o número:')
    this.valor = int(input())

#input exercício 15
def inputExer15():
    for i in range (11):
        print('Informe o valor {}'.format(i))
        num = int(input())
        resul = modelExercicios.exer15(num)
    print('{} números negativos'.format(resul))

#input exercício 16
def inputExer16():
    for i in range (11):
        print('Informe o valor {}'.format(i))
        this.valor = int(input())
        resoma = modelExercicios.exer16(this.valor)
    print('O resultado da soma é: {}'.format(resoma))

#input exercício 17
def inputExer17():
    print("Media Aritmética: {}".format(modelExercicios.exer17()))

def inputExer18():
    this.num = int(input("Digite aqui a quantidade de números que você irá digitar: "))
    lista = []
    digitados = 0
    total = 0
    while digitados < this.num:
        num = int(input("Digite aqui o " + str((digitados + 1)) + "°" + " número: "))
        lista.append(num)
        total = total + num
        digitados = digitados + 1

    lista.sort()
    print("A média aritmética dos números digitados é: " + str(total / len(lista)))
    print("O maior número é: " + str(lista[len(lista) - 1]))

#mostrar na tela
def mostrar():
    menu()
    if(this.opcao == 1):
        print(modelExercicios.exer1())

    elif(this.opcao == 2):
        inputExer2()
        print('O antecessor de {} é: {}'.format(this.valor, modelExercicios.exer2(this.valor)))

    elif(this.opcao == 3):
        inputExer3()
        print('A área do retângulo de base {} e altura {} é: {}'.format(this.base, this.altura, modelExercicios.exer3(this.base, this.altura)))

    elif (this.opcao == 4):
        inputExer4()
        print('Você viveu um total de {}'.format(modelExercicios.exer4(this.ano, this.mes, this.dia)), 'dias')

    elif (this.opcao == 5):
        inputExer5()
        print('O total de eleitores é: {} \n'.format(this.elei))
        print('Votos brancos: {} \n'.format(this.bran))
        print('Votos nulos: {} \n'.format(this.nulo))
        print('Votos válidos: {} \n'.format(this.vali))
        print('Os votos equivalem respectivamente a {}%'.format(modelExercicios.exer5(this.elei, this.bran, this. nulo, this.vali)), 'em relação ao total de eleitores')

    elif (this.opcao == 6):
        inputExer6()
        print('O salário é: {} \n'.format(this.sala))
        print('O reajuste é: {} \n'.format(this.reaj))
        print('O salário + reajuste é {} \n'.format(modelExercicios.exer6(this.sala, this.reaj)))

    elif (this.opcao == 7):
        inputExer7()
        print('O valor de fábrica ({}) somado com o percentual do distribuidor (28%) e os impostos (45%) é: {} \n'.format(this.valor, modelExercicios.exer7(this.valor)))

    elif (this.opcao == 8):
        inputExer8()
        print('A média do aluno {} é: {}'.format(this.aluno, modelExercicios.exer8(this.nota1, this.nota2, this.nota3)))

    elif (this.opcao == 9):
        inputExer9()
        print('A quantidade de maçãs é: {} e o custo total é: R${}'.format(this.maca, modelExercicios.exer9(this.maca)))

    elif (this.opcao == 11):
        inputExer11()
        print('O salário total é: {}'.format(modelExercicios.exer11(this.fixo, this.venda)))

    elif (this.opcao == 12):
        inputExer12()
        print('A sua conta possui: {}'.format(modelExercicios.exer12(this.nConta, this.saldo, this.debito, this.credito)))

    elif (this.opcao == 13):
        inputExer13()
        print(format(modelExercicios.exer13(this.tabuada)))

    elif (this.opcao == 14):
        inputExer14()
        print(format('Os valores inteiros até {} são: {}'.format(this.valor, modelExercicios.exer14(this.valor))))

    elif (this.opcao == 15):
        inputExer15()

    elif (this.opcao == 16):
        inputExer16()

    elif (this.opcao == 17):
        inputExer17()

    elif (this.opcao == 18):
        inputExer18()