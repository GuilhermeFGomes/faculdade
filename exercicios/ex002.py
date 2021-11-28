nome = input('digite seu nome:')
print('É um prazer te conhecer, {}!'.format(nome))
ano = int(input('em que ano vc nasceu ?'))
idadevirtual = (2021 - ano)
simounao = input('Sua idade é  {}?'.format(idadevirtual))

if simounao == 'sim':
    print('parabens')
else:
   mes = input('qual mes vc nasceu?')
   dia = input('qual dia vc nasceu?')