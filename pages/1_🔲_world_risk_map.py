import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """

    """
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html = True)

st.sidebar.title("Xenox")
st.sidebar.info(
    """
    
    """
)
with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.add_basemap("Stamen.Terrain")
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)



