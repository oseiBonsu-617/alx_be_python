FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def  convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    temperature = int(input("Enter the temperature to convert: "))
    celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if celsius_or_fahrenheit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f'{temperature}°C is {fahrenheit}°F')

    elif celsius_or_fahrenheit == "F":
        celsius = convert_to_celsius(temperature)
        print(f'{temperature}°F is {celsius}°C')

    else:
        print("Enter a valid unit (C/F)")


if __name__ == "__main__":
    main()

