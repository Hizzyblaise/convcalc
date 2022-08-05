import streamlit as st
#This is new again and again
# Function to convert Dana to kilogrammes
def dantokilo(value):
    result = value * 5.0
    return result

# Function to convert Garawa to Kilogrammes
def gartokilo(value):
    result = value * 40.0
    return result

st.subheader('CONVERSION CALCULATOR')
def mainmenu():
    choice = st.selectbox(
        "What conversion do you like to perform? ",
        [
            "1.Convert from Dana to Kilogrammes",
            "2.Convert from Garawa to Kilogrammes"
        ]
    )
    return choice


choice = mainmenu()

ivalue = float(st.text_input("Enter the value you want to convert: "))

if choice == "1.Convert from Dana to Kilogrammes":
    st.write(str(ivalue) + " dana to Kg is " + str(dantokilo(ivalue)) + "kg")
elif choice == "2.Convert from Garawa to Kilogrammes":
    st.write(str(ivalue) + " garawa to Kg is " + str(gartokilo(ivalue)) + "kg")



