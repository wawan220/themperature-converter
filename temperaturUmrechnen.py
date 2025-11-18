#https://pythonbuch.com/aufgabensammlung.html#temperatur-umwandler

import modul_umrechnen

mu=modul_umrechnen

#umrech= [
#    [mu.celsiusInKelvin,"Celsius","Kelvin"], 
#    [mu.celsiusInFareinheit,"Celsius","Fahreinheit"],
#    [mu.kelvinInCelsius, "Kelvin", "Celsius"],
#    [mu.kelvinInFareinheit, "Kelvin","Fahreinheit"],
#    [mu.fareinheitInCelsius, "Fahreinheit", "Celsius"],
#    [mu.fareinheitInKelvin, "Fahreinheit","Kelvin"]
#         ]
#

print("gebe bitte ein was du berechnen möchtest: \n", 
                  "(1) Celsius - Kelvin \n",
                   "(2) Celsius - Fahreinheit \n",
                    "(3) Kelvin - Celsius \n",
                     "(4) Kelvin - Fahreinheit \n",
                      "(5) Fahreinheit - Celsius \n",
                       "(6) Fahreinheit - Kelvin \n" )

eingabe=int(input("Wähle 1-6: \n> "))
print(eingabe)
if eingabe > 0 and eingabe <= 6:
    print("gebe die zu umrechnende Themperatur an:")
    temperatur=float(input("> "))
#
  #  print(f" Umrechnung von {umrech[eingabe-1][1]} in {umrech[eingabe-1][2]} \n {umrech[eingabe-1][1]}: \t{temperatur}")
  #  print(f"{umrech[eingabe-1][2]}: \t{umrech[eingabe-1][0](temperatur)}")

 
    if eingabe == 1:
        print(f" Umrechnung von Celsius in Kelvin \n Celsius: \t{temperatur}")
        print(f"Kelvin: \t{mu.celsiusInKelvin(temperatur)}")
    elif eingabe == 2:
        print(f" Umrechnung von Celsius in Fareinheit \n Celsius: \t{temperatur}")
        print(f"Fareinheit:\t{mu.celsiusInFareinheit(temperatur)}")
    elif eingabe == 3:
        print(f" Umrechnung von Kelvin in Celsius \n Kelvin: \t{temperatur}")
        print(f"Celsius: \t{mu.kelvinInCelsius(temperatur)}")
    elif eingabe == 4:
        print(f" Umrechnung von Kelvin in Fareinheit \n Kelvin: \t{temperatur}")
        print(f"Fareinheit: \t{mu.kelvinInFareinheit(temperatur)}")
    elif eingabe == 5:
        print(f" Umrechnung von Fareinheit in Celsius \n Fareinheit: \t{temperatur}")
        print(f"Celsius: \t{mu.fareinheitInCelsius(temperatur)}")
    elif eingabe == 6:
        print(f" Umrechnung von Fareinheit in Kelvin \n Fareinheit: \t{temperatur}")
        print(f"Kelvin: \t{mu.fareinheitInKelvin(temperatur)}")
    else :
        print("!!!ungültige eingabe bitte starte erneut!!!")
        print("program wird beendet")   
else:
    print("Falsche eingabe")
    print("starte das program neu")
