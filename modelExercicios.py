import this

import controllerExercicios

val = 0
this.msg = ""
this.contador = 0

def exer1():
    a = 10
    b = 20
    c = 0

    if(a == 10):
        c = a
        a = b
        b = c
        return 'A variável A possui {} e a variável B possui {}'.format(a, b)
    else:
        a = 10
        b = 20
        c = 0
        return 'Valores padrões'

def exer2(valor):
    return valor - 1

def exer3(base, altura):
    return base * altura

def exer4(ano, mes, dia):
    anoAtual = 2022
    mesAtual = 5
    diaAtual = 3

    dataAno = anoAtual - ano
    dataMes = mesAtual - mes
    dataDia = diaAtual - dia

    this.val = (dataAno * 365) + (dataMes * 30) + dataDia
    return val

def exer5(elei, bran, nulo, vali):
    votBran = bran * 100 / elei
    votNulo = nulo * 100 / elei
    votVali = vali * 100 / elei
    return votBran, votNulo, votVali

def exer6(sala, reaj):
    reaj = reaj / 100 #transforma porcentagem em número decimal
    aume = reaj * sala
    total = aume + sala
    return total

def exer7(valor):
    dist = valor * 28 / 100
    impo = valor * 45 / 100
    total = valor + impo + dist
    return total

def exer8(nota1, nota2, nota3):
    final = (nota1 + nota2 + nota3) // 3
    return final

def exer9(maca):
    if(maca < 12):
        preco = 1.30 * maca
    elif(maca >= 12):
        preco = 1 * maca
    return preco

def exer11(fixo, venda):
    if(venda < 1500):
        fixo = fixo + venda * 3 / 100
        return fixo
    elif(venda >= 1500):
        fixo = fixo + venda * 5 / 100
        return fixo
    else:
        return 'Erro'

def exer11(fixo, venda):
    if(venda < 1500):
        fixo = fixo + venda * 3 / 100
        return fixo
    elif(venda >= 1500):
        fixo = fixo + venda * 5 / 100
        return fixo
    else:
        return 'Erro'

def exer12(nConta, saldo, debito, credito):
    saldoA = saldo - debito + credito

    if(saldoA >= 0):
        return saldoA, 'Saldo positivo'
    elif(saldoA < 0):
        return saldoA, 'Saldo negativo'
    else:
        return 'Erro'

def exer13(tabuada):
    if(tabuada <= 10):
        for i in range(11):
            this.msg = this.msg + '{} * {} = {}\n'.format(i, tabuada, i * tabuada)
        return this.msg

def exer14(valor):
    for i in range(valor):
        this.msg = this.msg + '{}\n'.format(i + 1)
    return this.msg

def exer15(num):
    if (num < 0):
        this.contador = this.contador + 1
        return this.contador
    else:
        return this.contador

def exer16(valor):
    if (this.valor < 40):
        this.contador = this.contador + this.valor
    return this.contador

def exer16(valor):
    if (this.valor < 40):
        this.contador = this.contador + this.valor
    return this.contador

def exer17():
    soma = 0
    intervalo = len(range(15, 101))

    for i in range(15, 101):
        soma += i

    media = soma / intervalo
    return media






    












