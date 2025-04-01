# Constant value for the speed of light (m/s)
C = 299792458  

def mass_to_energy():
    """Continuously reads mass input and calculates energy using E = m * C^2"""
    while True:
        try:
            # user interface
            mass = float(input("Enter kilos of mass (or type '0' to exit): "))

            # Exit condition
            if mass == 0:
                print("Exiting program. Goodbye!")
                break

            # Calculate energy using Einstein's equation
            energy = mass * C**2
            EMC = f"\033[1;3;4m{energy:.16e}\033[0m"

            # Display the result
            print("\ne = m * C^2...\n")
            print(f"m = {mass:.1f} kg")
            print(f"C = {C} m/s")
            print(f"{EMC} joules of energy!\n")  

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

if __name__ == "__main__":
    mass_to_energy()
