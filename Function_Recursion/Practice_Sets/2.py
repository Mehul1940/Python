# Celius To Ferenheit Conversion
def celcius_to_farenheit(celcius):  
    farenheit = (celcius * 9/5) + 32
    return farenheit

celcius = float(input("Enter the temperature in Celcius: "))
farenheit = celcius_to_farenheit(celcius)

print(f"{celcius} Celcius is equal to {farenheit} Farenheit")