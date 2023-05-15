import datetime
now = datetime.datetime.now()
date = now.strftime("%d/%m/%Y")
frase_mae = 'vou contar até...'
qtde_mae_disse = 0

if date == '14/05/2023':
    print('Feliz dia das mães! <3')

    while qtde_mae_disse < 10:
        print(frase_mae, qtde_mae_disse)
        qtde_mae_disse += 1
        if qtde_mae_disse == 10:
          print('se eu for ai e você...') #termine a frase..