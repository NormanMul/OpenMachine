import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """



st.sidebar.title("About")
st.sidebar.info(
    """
    Make Open Source for Science and Society
    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Xenox by OpenMachine
    """
)

st.sidebar.title("Support")
st.sidebar.info(
    """
    - - You are not IN the universe, you ARE the universe, an intrinsic part of it -
    """
)


st.title("OpenMachine")

st.markdown(
    """
    This multi-page web app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and open-source mapping libraries, 
    such as [leafmap](https://leafmap.org), [geemap](https://geemap.org), [pydeck](https://deckgl.readthedocs.io), and [kepler.gl](https://docs.kepler.gl/docs/keplergl-jupyter).
    """
)

st.info("Welcome to OpenMachine - Create tommorow beyond imagination - Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(hide_st_style, unsafe_allow_html = True)



row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/river.gif")    
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/spain.gif")
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/las_vegas.gif")
    
    
    

with row1_col2:
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/world.gif")
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/goes.gif")
    st.image("https://github.com/NormanMul/OpenMachine/raw/main/data/fire.gif")
