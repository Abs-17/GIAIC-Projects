# Mars gravity ratio compared to Earth
MARS_GRAVITY_RATIO = 0.378  

# user interface
earth_weight = float(input("Enter your weight on Earth (kg): "))

# Weight Calculation
mars_weight = earth_weight * MARS_GRAVITY_RATIO


print(f"Your weight on Mars would be: {round(mars_weight, 2)} kg")
