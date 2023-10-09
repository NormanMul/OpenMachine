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

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2021'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
