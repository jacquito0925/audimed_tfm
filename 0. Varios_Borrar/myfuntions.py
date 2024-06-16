def string_to_num_string(string):
    num_string=0
    for i in range(len(string)):
        num=int(ord(string[i]))
        #print(num)
        num_string=num_string+num
    #print('Este es el valor de la cadena: '+cadena+' '+str(num_cadena))
    return num_string