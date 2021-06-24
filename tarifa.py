# Rango en kWh     Precio  (Cup)	 
 	 	 	 
# 0-100	        	0.33	 
# 101-150      	    1.07	 
# 151-200     	    1.43	 
# 201-250	        2.46	 
# 251-300	        3.00	 
# 301-350	        4.00	 
# 351-400	        5.00	 
# 401-450	        6.00	 
# 451-500	        7.00	 
# 501-600	        9.20	 
# 601-700	        9.45	 
# 701-1000	        9.85	 
# 1001-1800	        10.80	 
# 1801-2600	        11.80	 
# 2601-3400	        12.90	 
# 3401-4200	        13.95	 
# 4201-5000	        15.00	 
# Más de 5000	    20.00	 
 

def calcularTarifa(consumo):
    saldo = 0
    l_inf=0
    l_sup=100
    tarifa=0.33
    if consumo >l_sup:
        saldo += (l_sup-l_inf)*tarifa
        l_inf=l_sup
        l_sup=150
        tarifa=1.07

        if consumo >l_sup:
            saldo += (l_sup-l_inf)*tarifa
            l_inf=l_sup
            l_sup=200
            tarifa=1.43

            if consumo >l_sup:
                saldo += (l_sup-l_inf)*tarifa
                l_inf=l_sup
                l_sup=250
                tarifa=2.46

                if consumo >l_sup:
                    saldo += (l_sup-l_inf)*tarifa
                    l_inf=l_sup
                    l_sup=300
                    tarifa=3.00

                    if consumo >l_sup:
                        saldo += (l_sup-l_inf)*tarifa
                        l_inf=l_sup
                        l_sup=350
                        tarifa=4.00
                        if consumo >l_sup:
                            saldo += (l_sup-l_inf)*tarifa
                            l_inf=l_sup
                            l_sup=400
                            tarifa=5.00

                            if consumo >l_sup:
                                saldo += (l_sup-l_inf)*tarifa
                                l_inf=l_sup
                                l_sup=450
                                tarifa=6.00

                                if consumo >l_sup:
                                    saldo += (l_sup-l_inf)*tarifa
                                    l_inf=l_sup
                                    l_sup=500
                                    tarifa=7.00
                                    
                                    if consumo >l_sup:
                                        saldo += (l_sup-l_inf)*tarifa
                                        l_inf=l_sup
                                        l_sup=600
                                        tarifa=9.20
                                        
                                        if consumo >l_sup:
                                            saldo += (l_sup-l_inf)*tarifa
                                            l_inf=l_sup
                                            l_sup=700
                                            tarifa=9.45

                                            if consumo >l_sup:
                                                saldo += (l_sup-l_inf)*tarifa
                                                l_inf=l_sup
                                                l_sup=1000
                                                tarifa=9.85

                                                if consumo >l_sup:
                                                    saldo += (l_sup-l_inf)*tarifa
                                                    l_inf=l_sup
                                                    l_sup=1800
                                                    tarifa=10.80

                                                    if consumo >l_sup:
                                                        saldo += (l_sup-l_inf)*tarifa
                                                        l_inf=l_sup
                                                        l_sup=2600
                                                        tarifa=11.80

                                                        if consumo >l_sup:
                                                            saldo += (l_sup-l_inf)*tarifa
                                                            l_inf=l_sup
                                                            l_sup=3400
                                                            tarifa=12.90

                                                            if consumo >l_sup:
                                                                saldo += (l_sup-l_inf)*tarifa
                                                                l_inf=l_sup
                                                                l_sup=4200
                                                                tarifa=13.95

                                                                if consumo >l_sup:
                                                                    saldo += (l_sup-l_inf)*tarifa
                                                                    l_inf=l_sup
                                                                    l_sup=5000
                                                                    tarifa=15.00
                                                                    
                                                                    if consumo >l_inf & consumo<l_sup:
                                                                        saldo += (l_sup-l_inf)*tarifa
                                                                        l_inf=l_sup
                                                                        tarifa=20.00

                                                                        if consumo >l_inf:
                                                                            saldo += (l_sup-l_inf)*tarifa
                                                                            l_inf=l_sup
                                                                            tarifa=20.00
                                                                    
                                                                    else :
                                                                        saldo +=(consumo-l_inf)*tarifa
                                                                else :
                                                                    saldo +=(consumo-l_inf)*tarifa
                                                            else :
                                                                saldo +=(consumo-l_inf)*tarifa
                                                        else :
                                                            saldo +=(consumo-l_inf)*tarifa
                                                    else :
                                                        saldo +=(consumo-l_inf)*tarifa
                                                else :
                                                    saldo +=(consumo-l_inf)*tarifa
                                            else :
                                                saldo +=(consumo-l_inf)*tarifa
                                        else :
                                            saldo +=(consumo-l_inf)*tarifa
                                    else :
                                        saldo +=(consumo-l_inf)*tarifa
                                else :
                                    saldo +=(consumo-l_inf)*tarifa
                            else :
                                saldo +=(consumo-l_inf)*tarifa
                        else :
                            saldo +=(consumo-l_inf)*tarifa
                    else :
                        saldo +=(consumo-l_inf)*tarifa
                else :
                    saldo +=(consumo-l_inf)*tarifa
            else :
                saldo +=(consumo-l_inf)*tarifa
        else :
            saldo +=(consumo-l_inf)*tarifa
    else :
        saldo = consumo*tarifa
        
    print("Importe de la tarifa electrica: {} cup".format(saldo))
    return saldo




