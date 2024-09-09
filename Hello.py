import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="",
)

st.sidebar.header("Hello")
# create a space title with 2 columns
col_icone, col_title = st.columns([1, 5]) #ratio to set the distance between the title and logo
# display the image in front of the title
with col_icone:
    image_path='media/ship_vision.png'
    st.image(image_path,width=120)

with col_title:
    st.title("Ship Detection in Satellite Images")
st.markdown(
    """

"""
)
