
# Lautaro Ignacio Arias

def factorizar_numero(num):
    factores = []
    divisor = 2 
    while divisor <= num: 
        if num % divisor == 0: 
            factores.append(divisor)
            num //= divisor
        else: 
            divisor += 1
    return factores


def obtener_factores_comunes(numeros): 
    factores_comunes = []
    contador_factores = {}
    for num in numeros: 
        factores = factorizar_numero(num)
        contador_factores[num] = {}
        for factor in factores: 
            if factor in contador_factores[num]:
                contador_factores[num][factor] += 1 
            else: 
                contador_factores[num][factor] = 1    
            if factor not in factores_comunes: 
                factores_comunes.append(factor)
    return factores_comunes, contador_factores


def obtener_mcm(num1,num2,num3,num4):
    numeros = []
    numeros.append(num1)
    numeros.append(num2)

    factores_comunes, contador_factores = obtener_factores_comunes(numeros)
    mcm = 1
    for factor in factores_comunes:
        max_contador = 0
        for num in numeros: 
            contador = contador_factores[num].get(factor, 0)
            if contador > max_contador: 
                max_contador = contador
        mcm = mcm * factor ** max_contador
        
        
    # Cambio de valor en el caso de que num3 sea > a num4
    if(num3 > num4):
        temp = num4
        num4 = num3
        num3 = temp

    if(mcm >= num3 and mcm <= num4):
        result = mcm
    else:
        result = 0        
        
    return result



num1 = 60 # Calcular mcm
num2 = 54 # Calcular mcm
num3 = 10 # Extremo de Intervalo
num4 = 600 # Extremo de Intervalo

x = obtener_mcm(num1,num2,num3,num4)
print("El mcm entre los números",num1, "y", num2, "es:", x, ",respetando el intervalo: (", num3,">=x<=",num4, ")")
