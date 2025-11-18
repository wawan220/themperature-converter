def celsiusInFareinheit(temper):
    temperature= temper * 9/5 + 32
    return temperature

def celsiusInKelvin(temper):
    temperature= temper +273.15
    return temperature

def kelvinInCelsius(temper):
    temperature=temper -273.15
    return temperature

def kelvinInFareinheit(temper):
    temperature=celsiusInFareinheit(kelvinInCelsius(temper))
    return temperature

def fareinheitInCelsius(temper):
    temperature=5/9 * (temper-32)
    return temperature

def fareinheitInKelvin(temper):
    temperature=celsiusInKelvin(fareinheitInCelsius(temper))
    return temperature
