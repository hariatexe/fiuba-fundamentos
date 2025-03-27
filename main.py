def mcm(num1, num2, num3, num4):
    if(num2 > num1): 
        num_mayor = num2 
    else: 
        num_mayor = num1 
    
    if num3 > num4: 
        temp = num4
        num4 = num3
        num3 = temp


    while(num_mayor % num1) != 0 or (num_mayor % num2) != 0: 
        num_mayor += 1

    if(num3 <= num_mayor <= num4):
        result = num_mayor 
    else: 
        result = 0

    return result


print(mcm(10,20,10,700))