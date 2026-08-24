def calculate_voltage(current, resistance):
    """Calculate voltage using V = I × R."""
    return current * resistance


def calculate_current(voltage, resistance):
    """Calculate current using I = V / R."""
    if resistance == 0:
        raise ValueError("Resistance cannot be zero.")
    return voltage / resistance


def calculate_resistance(voltage, current):
    """Calculate resistance using R = V / I."""
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current


def get_number(prompt):
    """Get a valid positive number from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter a positive value.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=" * 40)
    print("       OHM'S LAW CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose what you want to calculate:")
        print("1. Voltage (V)")
        print("2. Current (I)")
        print("3. Resistance (R)")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        try:
            if choice == "1":
                current = get_number("Enter current (A): ")
                resistance = get_number("Enter resistance (Ω): ")

                voltage = calculate_voltage(current, resistance)

                print(f"\nVoltage = {voltage:.2f} V")

            elif choice == "2":
                voltage = get_number("Enter voltage (V): ")
                resistance = get_number("Enter resistance (Ω): ")

                current = calculate_current(voltage, resistance)

                print(f"\nCurrent = {current:.2f} A")

            elif choice == "3":
                voltage = get_number("Enter voltage (V): ")
                current = get_number("Enter current (A): ")

                resistance = calculate_resistance(voltage, current)

                print(f"\nResistance = {resistance:.2f} Ω")

            elif choice == "4":
                print("\nThank you for using the Ohm's Law Calculator!")
                break

            else:
                print("\nInvalid choice. Please select 1, 2, 3, or 4.")

        except ValueError as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
