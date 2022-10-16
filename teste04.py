#  5+3*2=11
#  5**2=25 | potenciação
#  5**3=125 | potenciação
#  19//2=9 | divisão exata
#  19/2=9.5 | divisão
#  18%2=0 | resto da divisão
#  122%3=2 | resto da divisão
#  4**3=64 | potenciação
#  pow(4,3)=64 | potenciação
#  81**(1/2)=9.0 | Raiz quadrada
#  25**(1/2)=5.0 | Raiz quadrada
#  127**(1/3)=5.026525......... | Raiz cubica

#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer {:=^20}!!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {}, a divisão inteira é {}, a exponenciação é {}'.format(s,sub,m,d,di,e))
