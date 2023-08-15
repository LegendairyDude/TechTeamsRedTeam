import streamlit as st
from streamlit_folium import st_folium
from streamlit_extras.colored_header import colored_header
import streamlit.components.v1 as components
import time
import folium
from folium import plugins

colored_header(
    label="Map",
    description=" ",
    color_name="violet-70",
)

st.sidebar.success("Please select a page.")

left_col, right_col = st.columns([150,50])


if st.button('Click to view map'):
    with st.spinner(text='In progress'):
        with left_col:
            time.sleep(3)
            map_test = folium.Map(location = [49.1852,-57.4184])
            folium.Marker([49.1852, -57.4184], popup='<i>Deer Lake</i>', tooltip='click me').add_to(map_test)
            #folium.Marker([48.9523, -57.9460], popup='<i>Corner Brook</i>', tooltip='click me').add_to(map_test)
            #folium.Circle(location=[48.9523, -57.9460], radius=200, popup='<i>Corner Brook</i>',tooltip='click me').add_to(m)
            plugins.Draw().add_to(map_test)
            st_map = st_folium(map_test, width = 850, height = 600, returned_objects=['last_onject_clicked'])
        with right_col:
            with st.expander("See Legend"):
                HtmlFile = open("legend.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code, height = 765)
