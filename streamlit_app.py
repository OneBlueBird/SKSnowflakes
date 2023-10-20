# Created main python file
import streamlit
import pandas
import requests;
import snowflake.connector;

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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
## streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

## The below line will pre-select Fruits and keep it ready. You can de-select a fruit
fruits_selected = streamlit.multiselect('Pick some fruits: ', list(my_fruit_list.index),['Apple', 'Avocado', 'Banana', 'Cantaloupe', 'Grapefruit', 'Grapes', 'Honeydew', 'Kiwifruit', 'Lemon', 'Lime', 'Nectarine', 'Orange', 'Peach', 'Pear', 'Pineapple', 'Plums', 'Strawberries', 'Cherries', 'Tangerine', 'Watermelon']);

## The below line will collect fruits a user selects and then display them accordingly
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

streamlit.header('Fruityvise Fruit Advice');
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi");
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

## -- SNOWFLAKE CONNECTION STARTS HERE --
## my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
## my_cur = my_cnx.cursor()
## my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
## my_data_row = my_cur.fetchone()
## streamlit.text("Hello from Snowflake:")
## streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor();
my_cur_execute("select * from fruit_load_list");
my_data_row = my_cur.fetchone();
streamlit.text("The fruit load list contains");
streamlit.text(my_data_row);


