import leafmap.plotlymap as leafmap
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

m = leafmap.Map()
m.add_basemap("Stamen.Terrain")
m.add_heatmap_demo()
m.add_scatter_plot_demo()
m.show()
