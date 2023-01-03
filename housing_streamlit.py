# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from crypto_wallet import generate_account
from crypto_wallet import get_balance
from crypto_wallet import send_transaction
w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


# Create login page for app
import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")


# Create background photo
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background2.jpeg') 


# Create a database of the houses

housing_database = {
    "House 1": [
        "House 1",
        "0x8cc4Ec1EA20817eA429F72Bf425DAeFd7Fe6D327",
        "19130 Cartwright Ct, Bend, OR 97702",
        100,
        "Images/house1.jpeg",
        "4,764 sqft",
        "4 Bed, 6 Bath",
    ],
    "House 2": [
        "House 2",
        "0x724C80B21588d4bE80157166729AE5D24C8e2855",
        "8641 Ruette Monte Carlo, La Jolla, CA 92037",
        200,
        "Images/house2.jpeg",
        "7,264 sqft",
        "5 Bed, 5 Bath",
    ],
    "House 3": [
        "House 3",
        "0x2415eE96a82dA6Bb14B35Fd0F396914965a7891B",
        "21376 N 110th Pl, Scottsdale, AZ 85255",
        250,
        "Images/house3.jpeg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 4": [
        "House 4",
        "0x1099C08D73BedF05026ea678D4B59087a8143d34",
        "5637 N 110th Pl, Scottsdale, AZ 85255",
        250,
        "Images/house4.jpg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 5": [
        "House 5",
        "0x0fF7CECF9C980A26cA8C9269a1158C1E63b785DB",
        "4227 N Burnham Pl, Scottsdale, AZ 85255",
        250,
        "Images/house5.jpg",
        "8,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 6": [
        "House 6",
        "0x04E537653B57753CfEbf4f03DC9144D22905259F",
        "1001 W Country Rd, Scottsdale, AZ 85255",
        250,
        "Images/house6.jpg",
        "9,600 sqft",
        "5 Bed, 6 Bath",
    ],
    "House 7": [
        "House 7",
        "0x3CE50A84bA63B1Ca28117E3c1Ff16dbd8E67FB02",
        "4227 N Burnham Pl, Scottsdale, AZ 85255",
        250,
        "Images/house7.jpg",
        "10,600 sqft",
        "5 Bed, 6 Bath",
    ]
}

# A list of houses
house = ["House 1", "House 2", "House 3", "House 4", "House 5", "House 6", "House 7"]

# Function to display housing data to streamlit
def get_house():
    
    db_list = list(housing_database.values())

    for number in range(len(house)):
        st.image(db_list[number][4], width=800)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write(db_list[number][2])
        st.write("Price ", db_list[number][3], "eth")
        st.write("Size ", db_list[number][5])
        st.write("Layout ", db_list[number][6])
        st.text(" \n")

# Create Header for Streamlit
st.markdown("# Welcome to the Block!")
st.markdown("## Blockchain Real Estate Market")
st.markdown("### Select a Home for Sale")
st.text(" \n")

# Create Sidebar
st.sidebar.markdown("##  House Account Address and Ethernet Balance in Ether")

# Call the generate_account function from cyrpto_wallet.py
account = generate_account()

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

# Display balance of account adress on side bar
st.sidebar.write(get_balance(w3, account.address))

# Create a select box to chose a house
houses = st.sidebar.selectbox("Select a House", house)

st.sidebar.markdown("## House, Price, and Ethereum Address")

# Identify the houses
place = housing_database[houses][0]

# Write the name of the house in the sidebar
st.sidebar.write(place)

# Identify the price
price = housing_database[houses][3]

# Write the in the price of the house to sidebar
st.sidebar.write(price)

# Identify the houses Ethereum Address
house_address = housing_database[houses][1]

# Write the houses Ethereum Address to the sidebar
st.sidebar.write(house_address)

# Sidebar Streamlit
st.sidebar.markdown("## Total Amount in Ether")

# Create the transcation hash
if st.sidebar.button("Send Transaction"):

    transaction_hash = send_transaction(w3, account, house_address, price)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

get_house()

