import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.info(
    """

    """
)

st.sidebar.title("Xenox")
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

def app():
    st.title("Search Basemaps")
    st.markdown(
        """
   
    """
    )

    with st.expander("See demo"):
        st.image("https://i.imgur.com/0SkUhZh.gif")

    row1_col1, row1_col2 = st.columns([3, 1])
    width = 800
    height = 600
    tiles = None

    with row1_col2:

        checkbox = st.checkbox("Search Quick Map Services (QMS)")
        keyword = st.text_input("Enter a keyword to search and press Enter:")
        empty = st.empty()

        if keyword:
            options = leafmap.search_xyz_services(keyword=keyword)
            if checkbox:
                qms = leafmap.search_qms(keyword=keyword)
                if qms is not None:
                    options = options + qms

            tiles = empty.multiselect(
                "Select XYZ tiles to add to the map:", options)

        with row1_col1:
            m = leafmap.Map()

            if tiles is not None:
                for tile in tiles:
                    m.add_xyz_service(tile)

            m.to_streamlit(height=height)


app()
