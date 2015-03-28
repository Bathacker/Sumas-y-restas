from random import randrange

def jugar(intento = 1):
    
    a = randrange(10)
    b = randrange(10)
    d = randrange(10)
    
    print ("\n DEMUESTRA TU INGENIO Y GANA!!")
    print (str(a)  + " * " + str(b) + " + " + str(d) + " = ")
    respuesta = raw_input('\n DAME EL RESULTADO: ') 
    
    if str(respuesta) != str((a*b)+d): 
        
        if intento < 3: 
            print "\n Fallaste Intentalo de nuevo" 
            intento += 1
            jugar(intento) # Llamada recursiva 
        
        else:
            print "\n Eres muy TONTO te equivocaste 3 veces Perdiste!" 
    
    else:
        print "\n Correcto!"
        intento = 1
        jugar(intento) # Llamada recursiva 

print 'Preparado'
jugar()