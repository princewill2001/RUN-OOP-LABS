# WILLIAMS PRINCEWILL GODWIN
# RUN/CMP/21/10947
# COMPUTER SCIENCE

# CONVERTING FROM FAHRENHEIT TO CELSIUS
def fahrenheit_tocelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius
    
# CONVERTING FROM CELSIUS TO FAHRENHEIT
def celsius_tofahrenheitahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit

if __name__ == '__main__':
    print(fahrenheit_tocelsius(120))
    print(celsius_tofahrenheitahrenheit(120))