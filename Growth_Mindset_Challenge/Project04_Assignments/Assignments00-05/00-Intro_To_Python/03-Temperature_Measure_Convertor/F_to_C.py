def fahrenheit_to_celsius():
    print("Temperature Converter: Fahrenheit to Celsius")
    
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: \033[1;3m{degrees_fahrenheit}F\033[0m = {degrees_celsius}C")


if __name__ == "__main__":
    fahrenheit_to_celsius()
