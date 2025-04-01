def main():
    print("The Triangle`s Perimeter Calculator")
     
    side01 = float(input("What is the length of Side 01? "))
    side02 = float(input("What is the length of Side 02? "))
    side03 = float(input("What is the length of Side 03? "))

    Perimeter_of_Triangle = f"\033[1;3m{str(side01 + side02 + side03)}\033[0m"
    print(f"The Calculated Perimeter of Triangle is {Perimeter_of_Triangle}")

if __name__ == '__main__':
    main()
    