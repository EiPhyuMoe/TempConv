import streamlit as st


st.title("Temperature Convertion")
option = st.selectbox(
    'How would you like to change temperature degrees?',
    ('Fahrenheit to Celsius', 'Celsius to Fahrenheit'),
)

if(option == 'Fahrenheit to Celsius'):
    degreesF = st.number_input("Enter the temperature in degrees F:",step=1)
    degreesC = 5/9*(float(degreesF) - 32)
    st.write(degreesF,"Degrees Fahrenheit is",degreesC,"Degrees Celsius")
else:
    degreesC = st.number_input("Enter the temperature in degrees C:",step=1)
    degreesF = 9/5* (float(degreesC))+32
    st.write(degreesC,"Degrees Celsius is",degreesF,"degrees Fahrenheit")

if(st.checkbox("Would you like to know formula?")):
    st.latex(r'''C = \dfrac{5}{9}(F - 32) ''')
    st.text("F = Degrees Fahrenheit")
    st.text("C = Degrees Celsius")
# this is the end of code.
# Thank you.
