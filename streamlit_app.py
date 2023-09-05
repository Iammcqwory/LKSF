import streamlit as st
import pandas as pd
import requests
from PIL import Image

# Define the functions to filter the fashion data, generate outfit ideas, create shopping lists, and find the perfect outfit
def filter_fashion_data(fashion_data, selected_style, selected_color):
  """
  Filters the fashion data based on user preferences.

  Args:
    fashion_data: The fashion data.
    selected_style: The selected style.
    selected_color: The selected color.

  Returns:
    The filtered fashion data.
  """

  filtered_data = fashion_data[(fashion_data['Style'] == selected_style) & (fashion_data['Color'] == selected_color)]

  return filtered_data

def generate_outfit_ideas():
  """Generates outfit ideas based on the user's input."""
  # Get the user's input
  top_category = st.selectbox("Top category:", ["Top", "Bottom", "Shoes"])

  # Generate the outfit ideas
  outfit_ideas = []
  for item in df[df["top_category"] == top_category]["item_name"]:
    outfit_ideas.append([item])

  # Display the outfit ideas
  st.table(outfit_ideas)

def create_shopping_list():
  """Creates a shopping list of the user's desired items."""
  # Get the user's input
  items = st.multiselect("Items:", df["item_name"].unique())

  # Create the shopping list
  shopping_list = [item for item in items]

  # Display the shopping list
  st.write("Shopping list:")
  st.list(shopping_list)

def find_perfect_outfit():
  """Finds the perfect outfit for a specific occasion based on the user's input."""
  # Get the user's input
  occasion = st.selectbox("Occasion:", ["Work", "Party", "Date", "Casual"])

  # Find the perfect outfit
  perfect_outfit = []
  for item in df[df["occasion"] == occasion]["item_name"]:
    perfect_outfit.append([item])

  # Display the perfect outfit
  st.table(perfect_outfit)

# Main function
def main():
  """The main function of the Streamlit app."""

  # Load the fashion data
  fashion_data = pd.read_csv("fashion_data.csv")

  # Sidebar
  st.sidebar.header('User Preferences')
  selected_style = st.sidebar.selectbox('Select Style', fashion_data['Style'].unique())
  selected_color = st.sidebar.selectbox('Select Color', fashion_data['Color'].unique())

  # Filter the fashion data
  filtered_data = filter_fashion_data(fashion_data, selected_style, selected_color)

  # Display the filtered fashion data
  if len(filtered_data) == 0:
    st.warning('No matching items found. Please adjust your preferences.')
  else:
    st.subheader('Recommended Fashion Items')
    st.write(filtered_data)

  # Buttons to generate outfit ideas, create shopping lists, and find the perfect outfit
  st.sidebar.button("Generate Outfit Ideas")
  st.sidebar.button("Create Shopping List")
  st.sidebar.button("Find Perfect Outfit")

  # Main content area
  if st.button("Generate Outfit Ideas"):
    generate_outfit_ideas()
  elif st.button("Create Shopping List"):
    create_shopping_list()
  elif st.button("Find Perfect Outfit"):
    find_perfect_outfit()

if __name__ == "__main__":
  main()
