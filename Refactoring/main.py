import modul_umrechnen

mu=modul_umrechnen


formelsammlung=[mu.celsius_in_kelvin , 
                mu.celsius_in_fahreinheit , 
                mu.kelvin_in_celsius , 
                mu.kelvin_in_fahreinheit , 
                mu.fahreinheint_in_celsius , 
                mu.fahreinheint_in_kelvin 
                ]

aufgabe=int(input("gebe eine Aufgabe ein z.B 1,2,3,4,5,6 usw....???"))
zahl1=float(input("gebe einen Zahl ein die du umrechnen möchtest:"))


#summe= formelsammlung[aufgabe-1](zahl1)
print (f"dein ergebnis ist: {formelsammlung[aufgabe-1](zahl1)}")