import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)

# Streamlit UI for BMI Calculator
def main():
    st.title("💪 BMI Calculator")
    st.write("Calculate your **Body Mass Index (BMI)** to understand your weight status.")

    # User Inputs
    weight = st.number_input("Enter your weight (kg):", min_value=20.0, max_value=200.0, step=0.1)
    height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, step=0.1)

    # BMI Calculation
    if st.button("Calculate BMI"):
        if weight and height:
            bmi_value = calculate_bmi(weight, height)

            st.success(f"✅ **Your BMI is:** {bmi_value}")

            # Display BMI category with quotes
            if bmi_value < 18.5:
                st.warning("⚠️ 'You are underweight.'")
            elif 18.5 <= bmi_value < 24.9:
                st.success("✅ 'You have a healthy weight.'")
            elif 25 <= bmi_value < 29.9:
                st.warning("⚠️ 'You are overweight.'")
            else:
                st.error("❌ 'You are obese.'")
        else:
            st.error("⚠️ Please enter valid values for weight and height.")

# Calling the main function to run the BMI app
if __name__ == "__main__":
    main()
