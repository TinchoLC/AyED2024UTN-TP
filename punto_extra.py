seq = input("Ingrese la cadena: ") # Secuencia(sequence) de colores, A(amarillo), V(verde) y R(rojo)
pos = int(input("Ingrese la posición en la que inicia: ")) # Position(posición) en la que empiezo
aux = -1 # Arranca en -1 para poder evaluar si hay una V antes de la posición que se ingresó
seqMax = 0 

if seq[pos] != "V": # Si es igual a V la secuencia es 0
    for i in range(pos): # Busca y almacena en aux la pos de la última V antes de la pos inicial
        if seq[i] == "V": 
            aux = i
    
    if aux != -1 : # Verifica si existe una V antes de la pos inicial
        seqMax = len(seq) - pos + aux # Al existir, entra en el resultante y cambia el número de la seqMax sacando la longitud de la cadena, le resta todos los números anteriores a la pos inicial y le suma la camtidad de pasos hasta V más lejana anterior a la pos
    else:
        for i in range (pos+1, len(seq)): # Al no haber cambiado el valor del aux, no existe una V previa a nuestra pos inicial y busca la V más lejana luego de nuestra pos inicial
            if seq[i] == "V": # Guarda la ubicación de la V más lejana si es que existe 
                aux = i
            
        seqMax = aux - pos # Calcula la seqMax restandole a la pos de la V más lejana con la pos inicial

if seqMax >= 0: # Asegura de que exista una V en la secuencia, ya que si no hay una V el aux nunca habría cambiado y al restarle un valor positivo a un valor negativo (-1 valor en que se inicializa aux) dará un número negativo o si en la pos inicial es una V entonces seqMax es 0 confimrando que V no existe
    print("La secuencia max es: ", seqMax) # Muestra la secuencia máxima encontrada, si en la posición inicial hay una V devuelve 0
else:
    print("No hay ninguna V en la secuencia, por lo tanto no existe la secuencia máxima de una posición a V")