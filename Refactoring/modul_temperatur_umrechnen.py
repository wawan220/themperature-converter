
def celsius_in_kelvin(temperatur):
    umrechn= temperatur + 273.15
    return umrechn

def celsius_in_fahreinheit(temperatur):
    umrechn= temperatur*9/5+32
    return umrechn

def kelvin_in_celsius(temperatur):
    umrechn= temperatur - 273.15
    return umrechn

def kelvin_in_fahreinheit(temperatur):
    #summe= zahl1 - 273.15 *9/5+32
    umrechn= kelvin_in_celsius(celsius_in_fahreinheit(temperatur))
    return umrechn

def fahreinheint_in_celsius(temperatur):
    #summe= zahl1 -32 /5*9
    umrechn= temperatur -32 /5*9
    return umrechn

def fahreinheint_in_kelvin(temperatur):
    #summe= zahl1 /5*9 + 273.15
    umrechn= celsius_in_kelvin(fahreinheint_in_celsius(temperatur))
    return umrechn

if __name__=="__main__":
    print(celsius_in_fahreinheit(500))