import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Get user input
number1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
number2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

# Select operation
operation = st.selectbox("Choose an operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Perform the calculation
if operation == "Add":
    result = number1 + number2
elif operation == "Subtract":
    result = number1 - number2
elif operation == "Multiply":
    result = number1 * number2
elif operation == "Divide":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("The result is:", result)
