def length_converter():
    print("\nLet's work with length!")
    meters = float(input("How many meters do you want to convert? "))
    print(f"{meters} meters is the same as:")
    print(f"   • {meters * 100:.2f} centimeters")
    print(f"   • {meters * 39.3701:.2f} inches")
    print(f"   • {meters * 3.28084:.2f} feet")

def weight_converter():
    print("\nTime to convert some weight!")
    kilograms = float(input("Enter the weight in kilograms: "))
    print(f"{kilograms} kilograms equals:")
    print(f"   • {kilograms * 1000:.2f} grams")
    print(f"   • {kilograms * 2.20462:.2f} pounds")
    print(f"   • {kilograms * 35.274:.2f} ounces")

def temperature_converter():
    print("\nLet's check the temperature conversions!")
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius} °C feels like:")
    print(f"   • {fahrenheit:.2f} °F")
    print(f"   • {kelvin:.2f} K")

def main():
    print("Welcome to your friendly Unit Converter!")
    while True:
        print("\nWhat would you like to convert today?")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        
        choice = input("Pick an option (1-4): ")
        
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Thanks for using the Unit Converter. Have a great day!")
            break
        else:
            print("Oops! That wasn’t a valid choice. Try again.")

if __name__ == "__main__":
    main()
