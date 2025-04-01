import time

def display_intro():
    """ An intro message for the launch sequence"""
    print("\n🌌 Welcome to the Space Launch Countdown System! 🚀\n")
    print("Prepare for an exciting countdown to liftoff!\n")

def countdown(start=10):
    """Counts down from a given number to 1, then prints Liftoff!"""
    for i in range(start, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)  
    print("🔥 Liftoff! 🚀\n")

def main():
    """ function to execute the space launch countdown"""
    display_intro()

    while True:
        start_count = input("Enter countdown start number (default is 10): ").strip()
        if start_count == "":
            start_count = 10  # Default value
        elif not start_count.isdigit() or int(start_count) <= 0:
            print("⚠️ Please enter a valid positive number!\n")
            continue
        
        start_count = int(start_count)
        print("\n🌍 Initiating countdown...\n")
        countdown(start_count)

        again = input("Do you want to launch again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n🛰️ Mission Control signing off. Have a great day! 🌟")
            break

if __name__ == "__main__":
    main()
