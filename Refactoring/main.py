import modul_temperatur_umrechnen

mtu=modul_temperatur_umrechnen

formelsammlung=[mtu.celsius_in_kelvin , 
                mtu.celsius_in_fahreinheit , 
                mtu.kelvin_in_celsius , 
                mtu.kelvin_in_fahreinheit , 
                mtu.fahreinheint_in_celsius , 
                mtu.fahreinheint_in_kelvin 
                ]

aufgabe=int(input("gebe eine Aufgabe ein z.B 1,2,3,4,5,6 usw....???"))

if aufgabe > 0 and aufgabe <=6:
    zahl1=float(input("gebe einen Zahl ein die du umrechnen möchtest:"))
    #summe= formelsammlung[aufgabe-1](zahl1)
    print (f"dein ergebnis ist: {formelsammlung[aufgabe-1](zahl1)}")
else:
    print("fehlerhafte eingabe bitte neustarten!")