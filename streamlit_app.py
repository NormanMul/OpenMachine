import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """

    """
)

st.sidebar.title("Contact")
st.sidebar.info(
    """
    
    """
)

# Customize page title
st.title("Geospatial Applications")

st.markdown(
    """
    
    """
)

st.header("Instructions")

markdown = """


"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
