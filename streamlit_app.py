# Created main python file
import streamlit
import pandas

## print("Hello, World - Streamlit");
streamlit.title('My Parents New Healthy Diner');

streamlit.header('Breakfast Menu');
streamlit.text('🥣 Omega 2 & Blueberry Oatmeal');
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔 Hard-Boiled Fre-Range Egg');
streamlit.text('🥑🍞 Avacado Toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## Here using Pandas library to retrieve data from AWS S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
