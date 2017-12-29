def hours2days(horas):
    dias = (horas/24)
    horas = (horas % 24)
    #print "Dias: {} Horas:{}".format( dias, horas)
    #return dias, horas

    return horas//24, horas % 24



#hours2days(39) # 24 horas é um dia e zero horas
print(hours2days(24)) # 24 horas é um dia e zero horas
#(1, 0)
print(hours2days(25)) # 25 horas é um dia e uma hora
#(1, 1)
print(hours2days(10000))
#(416, 16)