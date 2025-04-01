def elegir(actividades, actividades_deseadas, cuota):
    MAX_CUOTA = 6000 
    coincidencias = 0  
    i = 0 

    while i < len(actividades_deseadas) and coincidencias < 2:
        if actividades_deseadas[i] in actividades:  
            coincidencias += 1
        i += 1 

    return coincidencias >= 2 and cuota <= MAX_CUOTA

def main(): 
    lista_1 = ['natación', 'gimnasio', 'voley', 'futbol']
    lista_2 = ['natación', 'voley', 'gimnasio']
    lista_3 = ['natación', 'futbol', 'karate']
    print(elegir(lista_2,lista_3,100))

main()


