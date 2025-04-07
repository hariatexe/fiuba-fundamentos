def calcular_total_ventas(ventas):
    return sum(sum(sucursal) for sucursal in ventas)

def sucursal_con_menos_ventas(ventas):
    totales = [sum(sucursal) for sucursal in ventas]
    menor = min(totales)
    indice = totales.index(menor) # Obtiene la posicion del menor valor
    return indice + 1, menor # Suma uno, para obtener el numero de sucursal

def dia_con_mas_ventas(ventas):
    dias = list(zip(*ventas))  # Transpone la matriz para obtener las ventas del dia
    suma_por_dia = [sum(dia) for dia in dias]
    maximo = max(suma_por_dia)
    indice = suma_por_dia.index(maximo)
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    return dias_semana[indice], maximo

def main():
    ventas = [
        [100, 200, 300, 400, 500], 
        [1100, 1200, 1300, 1400, 1500],
        [10, 20, 30, 40, 50]
    ]

    total = calcular_total_ventas(ventas)
    sucursal, ventas_min = sucursal_con_menos_ventas(ventas)
    dia, monto_max = dia_con_mas_ventas(ventas)

    print("El total de ventas en la semana fue:", total)
    print(f"La sucursal {sucursal} tuvo menos ventas, VENTAS: {ventas_min}")
    print(f"El día con más ventas fue {dia} con un total de {monto_max}")

main()
