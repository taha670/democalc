import streamlit as st

# Set up the title of the web app
st.title("Simple Streamlit Calculator")

# Create input fields for the two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Create dropdown menu for the operation
operation = st.selectbox("Choose an operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the calculation based on the selected operation
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."

# Display the result
st.write(f"Result: {result}")
