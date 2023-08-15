import streamlit as st
import streamlit.components.v1 as components
import folium
from folium import plugins
from streamlit_extras.colored_header import colored_header
import time

colored_header(
    label="Map",
    description=" ",
    color_name="violet-70",
)

#st.info("This is a map for the west coast of NewfoundLand that has")

st.sidebar.success("Please select a page.")


m = folium.Map(location = [49.1852,-57.4184])
folium.Marker([49.1852, -57.4184], popup='<i>Deer Lake</i>', tooltip='click me').add_to(m)
#folium.Marker([48.9523, -57.9460], popup='<i>Corner Brook</i>', tooltip='click me').add_to(m)

#folium.Circle(location=[48.9523, -57.9460], radius=200, popup='<i>Corner Brook</i>',tooltip='click me').add_to(m)

plugins.Draw().add_to(m)

m.save('map.html')

col1, col2, col3, col4 = st.columns(4)

if st.button('Click to view map'):
    with st.spinner(text='In progress'):
        with col1:
            time.sleep(3)
            HtmlFile = open("map.html", 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            print(source_code)
            components.html(source_code, height = 600, width = 536)
            time.sleep(1)
        with col4:
            with st.expander("See Legend"):
                HtmlFile = open("legend.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code, height = 600)
