from cuentas import cuentas_list
from colorama import init, Fore, Back, Style
import random
import sys
import os

init()

def play():
    cuenta_random = get_random_cuenta()
    user_input = guess_clasification(cuenta_random)
    if int(user_input) != cuenta_random[1]:
        os.system('cls')
        print(Fore.RED + 'ERROR')
    else:
        os.system('cls')
        print(Fore.GREEN + 'CORRECTO')
        user_input = guess_rubro(cuenta_random)
        if int(user_input) != cuenta_random[2]:
            os.system('cls')
            print(Fore.RED +'ERROR')
        else: 
            os.system('cls')
            print(Fore.GREEN + 'CORRECTO')
            
def get_random_cuenta():
    ran = random.randint(0,len(cuentas_list))
    return cuentas_list[ran]
    
def guess_clasification(cuenta_random):
    print(Style.RESET_ALL + '---------------------------------')
    print('1. ACTIVO\n2. PASIVO\n3. PATRIMONIO NETO\n4. RESULTADO NEGATIVO\n5. RESULTADO POSITIVO')
    print('---------------------------------')
    user_input = input(f'{cuenta_random[0]}: ')
    return user_input
    
def guess_rubro(cuenta_random):
    if cuenta_random[1] == 1:
        print(Style.RESET_ALL + 'ACTIVO\n- Bienes de cambio 1\n- Bienes de uso 2\n- Bienes Intangibles 3\n- Cajas y Bancos 4\n- Creditos 5\n- Inversiones 6\n- Otros Creditos 7')
    elif cuenta_random[1] == 2:
        print(Style.RESET_ALL +'PASIVO\n- Deudas Comerciales 1\n- Deudas Financieras/Bancarias 2\n- Deudas Fiscales 3')
    elif cuenta_random[1] == 3:
        print(Style.RESET_ALL +'PATRIMONIO NETO\n- Capital Social 1\n- Reservas 2\n- Resultados 3')
    elif cuenta_random[1] == 4:
        print(Style.RESET_ALL + 'RESULTADO NEGATIVO:\n- Costo de Ventas 1\n- Egresos Extraordinarios 2\n- Gastos Financieros 3\n- Gastos Comerciales 4\n- Operativos 5')
    elif cuenta_random[1] == 4:
        print(Style.RESET_ALL + 'RESULTADO POSITIVO:\n- Ingresos Extraordinarios')
    user_input = input(f'{cuenta_random[0]}: ')
    return user_input
    
while True:
    try:
        play()
    except KeyboardInterrupt:
        os.system('cls')
        print(Fore.YELLOW + '\nGracias por JUGAR!!')
        sys.exit()
  