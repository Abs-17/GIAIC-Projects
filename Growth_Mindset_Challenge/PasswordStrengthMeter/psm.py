#Libraries
import re
import random
import string
import streamlit as st
import math

# Store password history
password_history = []

def generate_strong_password():
    words = ["Blue", "Tree", "Sky", "Ocean", "Cloud", "Storm", "Rock"]
    numbers = ''.join(random.choices(string.digits, k=2))
    special = random.choice("!@#$%^&*")
    return f"{random.choice(words)}{special}{random.choice(words)}{numbers}"

def calculate_entropy(password):
    unique_chars = len(set(password))
    entropy = len(password) * math.log2(unique_chars) if unique_chars > 1 else 0
    return entropy

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Common weak passwords blacklist
    weak_passwords = {"password", "123456", "password123", "qwerty", "abc123"}
    if password.lower() in weak_passwords:
        return "Weak", ["Avoid using common passwords."]
    
    # Check if password was used before
    if password in password_history:
        return "Weak", ["Avoid reusing old passwords."]
    
    # Check length
    if len(password) >= 8:
        score += 2  # Increased weight
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check uppercase and lowercase letters
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*]', password):
        score += 2  # Increased weight
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")
    
    # Calculate entropy for advanced strength measurement
    entropy = calculate_entropy(password)
    if entropy < 28:
        feedback.append("Increase password complexity to improve entropy.")
    
    # Assign strength level
    if score >= 5 and entropy >= 60:
        strength = "Strong"
    elif score >= 3 and entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Store password in history
    password_history.append(password)
    return strength, feedback

def main():
    st.set_page_config(page_title="PSM - Password Strength Meter", layout="wide", page_icon="🔐")
    st.markdown("""
        <style>
        body { background-color: #121212; color: white; }
        .stTextInput input { color: black; }
        </style>
        """, unsafe_allow_html=True)
    
    st.title("🔒 Password Strength Meter")
    password = st.text_input("Enter your password", type="password", key="password_input")
    
    if password:
        strength, feedback = check_password_strength(password)
        st.write(f"**Password Strength:** {strength}")
        
        if strength == "Weak":
            st.error("Your password is weak. Consider improving it!")
            st.write("### Suggestions to improve:")
            for tip in feedback:
                st.write(f"- {tip}")
            st.write(f"**Suggested strong password:** `{generate_strong_password()}`")
        elif strength == "Moderate":
            st.warning("Your password is okay but could be improved.")
        elif strength == "Strong":
            st.success("Your password is strong and secure!")
    
    if st.button("Generate Secure Passphrase"):
        st.write(f"**Suggested Passphrase:** `{generate_strong_password()}`")

if __name__ == "__main__":
    main()
