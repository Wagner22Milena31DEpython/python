verificação = int(input("digite seu numero de verificação"))
n1 = float(input("digite sua primeira nota"))
n2 = float(input("digite sua segunda nota"))
n3 = float(input("digite sua terceira nota"))
me = float(input("digite sua media de exercicios"))
ma = (n1  + n2 * 2 + n3 * 3 + me) / 7
if ma >= 90:
    print(verificação,n1,n2,n3,me,ma,"Aprovado, A")
elif ma >= 75 and ma < 90:
    print(verificação,n1,n2,n3,me,ma,"Aprovado, B")
if ma >= 60 and ma < 75:
    print(verificação,n1,n2,n3,me,ma,"Aprovado, C")
elif ma >= 40 and ma < 60:
    print(verificação,n1,n2,n3,me,ma,"Reprovado, D")
if ma < 40:
    print(verificação,n1,n2,n3,me,ma,"reprovado, E")