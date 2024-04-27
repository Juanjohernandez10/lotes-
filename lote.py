

ls_urbano = []
ls_comercial = []
ls_campestre = []

import os
def fnt_limpiar ():
    os.system('cls')
    print('----- AUTOR ----- JUAN JOSE HERNANDEZ --- ')
    print('----- UNIVERSIDAD CATOLICA LUIS AMIGÓ ---')
    print('----- 25 de abril del 2024 --------------')

def fnt_calcular_area(largo, ancho):
    area = largo * ancho
    return area

def fnt_determinar_valor(nombre,area, tipo):
    
    global pagar
    
    if tipo == 'urbano':
        valor = area * 25000
        permiso = valor * 0.45
        pagar = valor + permiso
        print(f'estimado usuario {nombre} el area es : {area}m2, el valor a pagar por todo es: ${pagar}')
        ls_urbano.append([nombre, area, valor, pagar])
    elif tipo == 'comercial':
        valor = area * 60000
        permiso = valor * 0.75
        pagar = valor + permiso
        print(f'estimado usuario {nombre} el area es : {area}m2, el valor a pagar por todo es: ${pagar}')
        ls_comercial.append([nombre, area, valor, pagar])
    elif tipo == 'campestre':
        valor = area * 15000
        permiso = valor * 0.15
        pagar = valor + permiso
        print(f'estimado usuario {nombre} el area es : {area}m2, el valor a pagar por todo es: ${pagar}')
        ls_campestre.append([nombre, area, valor, pagar])

def fnt_selector(op):
    global controlBln
    if op == 1:
        while True:
            fnt_limpiar()
            tipo = input('Ingrese el tipo de lote: ')
            if tipo == ' ' or tipo == ' ' or tipo == ' ':
                print(' la informacion es invalida')
                
            if tipo == 'urbano' or tipo == 'comercial' or tipo == 'campestre':
                nombre = input('ingrese su nombre -> ')
                largo = float(input('Ingrese el largo del lote: '))
                ancho = float(input('Ingrese el ancho del lote: '))
                area = fnt_calcular_area(largo, ancho)
                fnt_determinar_valor(nombre,area, tipo)
                print(' la informacion fue registrada')
                
            
            enter = input('Presione enter para continuar <ENTER>')
            break

            
    elif op == 2:
        fnt_limpiar()
        if len(ls_urbano) > 0:
                print('Lotes urbanos:')
                for i in range(len(ls_urbano)):
                    print(f'{ls_urbano[i]}')
        if len(ls_comercial) > 0:
                print('Lotes comerciales:')
                for i in range(len(ls_comercial)):
                    print(f'{ls_comercial[i]}')
        if len(ls_campestre) > 0:
                print('Lotes campestres:')
                for i in range(len(ls_campestre)):
                    print(f'{ls_campestre[i]}')
        enter = input('presione enter para continuar <ENTER>')
    elif op == 3:
        controlBln = False
        
  
    
    

controlBln = True
while controlBln ==True:
        fnt_limpiar()
        print('<<MENU>>')
        print('1. Registrar lote')
        print('2. Mostrar')
        print('3. Salir')
        op = int(input('Ingrese una opción: '))
        fnt_selector(op)
        