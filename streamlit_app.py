# Created main python file

# import streamlit
import streamlit

#import pandas
import pandas;

#import requests
import requests;

#import snowflake.connector
import snowflake.connector;

#import URLError
from urllib.error import URLError;

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

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.");
    else:
        streamlit.write('The user entered ', fruit_choice)
        streamlit.header('Fruityvise Fruit Advice');
 	back_from_funtion = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_funtion);
        ##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        ##fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
        ##streamlit.dataframe(fruityvice_normalized)      
        # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
        # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi");
        #  streamlit.text(fruityvice_response.json())
except URLError as e:
	streamlit.error();

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

## -- SNOWFLAKE CONNECTION STARTS HERE --
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor();
my_cur.execute("select * from fruit_load_list");
my_data_row = my_cur.fetchone();
streamlit.text("The fruit load list contains");
streamlit.text(my_data_row);

my_data_row = my_cur.fetchone();
streamlit.header("The fruit load list contains:");
streamlit.dataframe(my_data_row);

my_cur.execute("select * from fruit_load_list");
my_data_rows = my_cur.fetchall();
streamlit.header("The fruit load list contains:");
streamlit.dataframe(my_data_rows);


fruit_choice1 = streamlit.text_input('What fruit would you like Add ?','Kiwi')
streamlit.write('The user entered ', fruit_choice1);

streamlit.write('Thanks for adding', fruit_choice1);
## This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')");

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]);
my_cur = my_cnx.cursor();
my_cur.execute("select * from fruit_load_list");
my_data_rows = my_cur.fetchall();
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows);

# don't run anything past here while we troubleshoot
streamlit.stop();
