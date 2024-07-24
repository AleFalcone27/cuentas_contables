'''
ACTIVO: 1
- Bienes de cambio 1
- Bienes de uso 2
- Bienes Intangibles 3
- Cajas y Bancos 4
- Creditos 5
- Inversiones 6
- Otros Creditos 7

PASIVO: 2
- Deudas Comerciales 1
- Deudas Financieras/Bancarias 2
- Deudas Fiscales 3

PATRIMONIO NETO: 3
- Capital Social 1
- Reservas 2
- Resultados 3

RESULTADO NEGATIVO: 4
- Costo de Ventas 1 
- Egresos Extraordinarios 2
- Gastos Financieros 3
- Gastos Comerciales 4
- Gastos Operativos 5

RESULTADO POSTIVO: 5
- Ingresos Extraordinarios 1

[cuenta,ACTIVO/PASIVO/PN/RN/RP,rubro]

'''


cuentas_list = [
    
    ## ACTIVO
    
    # Bienes de cambio
    ['Mercaderias',1,1],['Materias Primas',1,1],['Productos Elaborados',1,1],['Amortizaciones Acumuladas de X (RESTA)',1,2],
    # Bienes de uso
    ['Rodados',1,2],['Muebles y Útiles',1,2],['Inmuebles',1,2],['Rodados',1,2],['Equipos Informaticos',1,2],['Instalaciones',1,2],['Maquinarias',1,2],
    # Bienes intangibles
    ['Franquicias',1,3],['Patentes',1,3],['Marcas',1,3],['Gastos de investigacion',1,3],
    # Caja y Bancos
    ['Banco x Cuenta Corriente',1,4],['Caja',1,4],['Cheques de Terceros',1,4],['Moneda Extranjera',1,4],
    # Creditos
    ['Deudores en Gestión judicial',1,5], ['Deudores morosos',1,5], ['Deudores por ventas',1,5], ['Documentos a cobrar',1,5], 
    ['Intereses Positivos a Devengar (RESTA)',1,5], ['Previsiones por Deudores Incobrables (RESTA)',1,5], ['Previsiones por descuentos',1,5],
    ['Servicios a cobrar',1,5], ['IVA Crédito Fiscal',1,5],
    # Inversiones
    ['Banco x Plazo Fijo',1,6], ['Titulos y Acciones',1,6], ['Fondos de Inversión',1,6], ['Inmuebles en Alquiler',1,6],
    # Otros creditos
    ['Alquileres Pagados por Adelantado',1,7], ['Alquileres a Cobrar',1,7], ['Anticipos a impuestos',1,7], ['Anticipos de Sueldos',1,7], 
    ['Seguros Pagados por Adelantado',1,7], ['Accionistas',1,7], ['Socio X Cuenta Aporte',1,7],
    
    ## PASIVO
    
    # Deudas Comerciales
    ['Prestamos Otorgados',2,1], ['Prendas a Pagar',2,1], ['Anticipo de Clientes',2,1], ['Documentos a pagar',2,1], ['Proveedores',2,1],
    ['Servicios a Pagar',2,1], ['Acreedores Varios',2,1], ['Alquileres a Pagar',2,1], ['Alquileres Cobrados por Adelantado',2,1],
    ['Comisiones a Pagar',2,1], ['Cuentas a Pagar',2,1], 
    # Deudas Financieras
    ['Intereses Negativos a Devengar (RESTA)',2,2], ['Obligaciones Negociables',2,2], ['Hipotecas a Pagar',2,2],
    # Deudas Fiscales
    ['Impuestos Adeudados',2,3], ['Ingresos Brutos a pagar',2,3], ['Cargas Sociales a Pagar',2,3], ['Impuestos a Pagar',2,3],
    ['Moratorias a Pagar',2,3], ['Sueldos a pagar',2,3], ['Previsiones para Despidos/Indemnizaciones',2,3],
    
    ## PATRIMONIO NETO
    ['Capital Social',3,1], ['Reservas Legales',3,2], ['Útilidades no Distribuidas',3,3],
    
    ## RESULTADO NEGATIVO
    # CMV
    ['CMV',4,1],
    # Egresos Extraordinarios
    ['Deudores Incobrables',4,2], ['Indemnizacion por Despidos',4,2], ['Diferencia negativa de Cotización',4,2],
    # Gastos Financieros
    ['Intereses perdidos',4,3],
    # Gastos Comerciales
    ['Gastos de Publicidad',4,4], 
    # Gastos operativos
    ['Amortizaciones',4,5], ['Gastos Generales',4,5], ['Gastos de Funcionamiento',4,5], ['Gastos Varios',4,5], ['Alquileres',4,5],
    ['Impuestoa a las Ganancias',4,5], ['Sueldos y Jornales',4,2],
    
    ## RESULTADO POSITIVO
    # Ingresos Extraordinarios
    ['Intereses Positivos/Ganados',6,1], ['Diferencia Positiva de cotización',6,1], ['Recupero de Previsión para Deudores Incobrables',6,1],
    ['Ventas',6,1],
    
]
    