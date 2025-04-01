import streamlit as st

# Initialize session state if it doesn't exist
if "income" not in st.session_state:
    st.session_state.income = []  # List to store income records

if "expenses" not in st.session_state:
    st.session_state.expenses = []  # List to store expense records

# Function to add income
def add_income(amount, description, category):
    if amount and description:
        st.session_state.income.append({"amount": amount, "description": description, "category": category})

# Function to add expense
def add_expense(amount, description, category):
    if amount and description:
        st.session_state.expenses.append({"amount": amount, "description": description, "category": category})

# Streamlit UI Setup
st.title("💰 Personal Finance Tracker")
st.write("Track your income, expenses, and balance for the month.")

# User Input for Income
st.subheader("Add Income")
income_amount = st.number_input("Enter income amount:", min_value=0.0, format="%.2f")
income_description = st.text_input("Enter a description for this income:")
income_category = st.text_input("Enter a category (e.g., Salary, Freelance):")

# Add Income Button
if st.button("Add Income"):
    add_income(income_amount, income_description, income_category)

# User Input for Expenses
st.subheader("Add Expense")
expense_amount = st.number_input("Enter expense amount:", min_value=0.0, format="%.2f")
expense_description = st.text_input("Enter a description for this expense:")
expense_category = st.text_input("Enter a category (e.g., Rent, Groceries):")

# Add Expense Button
if st.button("Add Expense"):
    add_expense(expense_amount, expense_description, expense_category)

# Display Summary
if st.session_state.income or st.session_state.expenses:
    st.subheader("📊 Summary")
    
    # Calculate total income and total expenses
    total_income = sum([item["amount"] for item in st.session_state.income])
    total_expenses = sum([item["amount"] for item in st.session_state.expenses])
    balance = total_income - total_expenses
    
    st.write(f"**Total Income:** ${total_income:.2f}")
    st.write(f"**Total Expenses:** ${total_expenses:.2f}")
    st.write(f"**Balance:** ${balance:.2f}")
    
    # Display Income Records
    if st.session_state.income:
        st.subheader("🤑 Income Records")
        for idx, record in enumerate(st.session_state.income):
            st.write(f"{idx+1}. **${record['amount']:.2f}** - {record['description']} (Category: {record['category']})")
    
    # Display Expense Records
    if st.session_state.expenses:
        st.subheader("💸 Expense Records")
        for idx, record in enumerate(st.session_state.expenses):
            st.write(f"{idx+1}. **-${record['amount']:.2f}** - {record['description']} (Category: {record['category']})")

else:
    st.write("No records to display. Add your income and expenses to get started.")

# Footer
st.markdown("""
---
Made with ❤️ by [Your Name](https://www.linkedin.com/in/yourname).
""")
