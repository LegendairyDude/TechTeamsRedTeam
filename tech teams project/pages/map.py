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
            folium.Marker([49.18897486046366, -57.422280490936096], icon = folium.Icon(color="darkpurple", icon="fa-wheelchair", prefix="fa"), popup='<i>Elite Kinetics & Training</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.940602631286495, -57.9724119020463], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Pharmasave Veitch Wellness Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.94391903886318, -57.946607922169925], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Lawtons Drugs</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.95134600052603, -57.95100187889012], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Sobeys Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.952472157804706, -57.950431271448075], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Shoppers Drug Mart</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.9520290047458, -57.946781800201], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Health and Performance Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.95260209862421, -57.94438500389429], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>City Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.95773075031993, -57.92395782619144], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>DRUGStore Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.96035747787567, -57.9235321081281], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Walmart Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.50440863799427, -58.43637590033207], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Skinners Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.54893331002188, -58.57933693460658], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Bens Pharmacy Limited</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.5055632799553, -58.437805161596266], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Pharmasave Sheas Pharmacy & Wellness</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.54602843055215, -58.57637585818335], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>DRUGStore Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.54946615675382, -58.57393498676838], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Shoppers Drug Mart</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.55003438613701, -58.57415535059746], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Walmart Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.555432921902685, -58.56516167728675], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Pharmasave Whites</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([49.019738188240964, -57.58241480407586], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>The Medicine Shoppe Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([49.582406832179885, -57.91059794433049], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Pharmasave Complete Care Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([49.03596743474425, -57.849616435249935], icon = folium.Icon(color="cadetblue", icon="fa-plus-circle", prefix="fa"), popup='<i>Sentrex Pharmacy</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([47.58891549151834, -59.16283100028992], icon = folium.Icon(color="lightred", icon="fa-plus-circle", prefix="fa"), popup='<i>Dr. Charles L. LeGrow Health Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([47.61403922905521, -57.622275544465865], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Calder Health Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([50.91358242741083, -57.09517001332259], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Rufus Guinchard Health Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.55959448697954, -58.552574484881575], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Sir Thomas Roddick Hospital</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.948333076679134, -57.930059263414634], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Western Memorial Regional Hospital</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.95165442924059, -57.95288295969275], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Downtown Health Center </i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([49.53686159776368, -57.87487142529385], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Bonne Bay Health Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.939179781454214, -57.93124466766429], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Corner Brook Long Term Care Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.50942338267729, -58.44527617324045], icon = folium.Icon(color="lightred", icon="fa-heartbeat", prefix="fa"), popup='<i>Bay St. George Long Term Care Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.95255262299959, -57.95013269935132], icon = folium.Icon(color="lightblue", icon="fa-bed", prefix="fa"), popup='<i>Griffin Pain Relief Clinic</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.940584384166556, -57.972228269513], icon = folium.Icon(color="lightblue", icon="fa-bed", prefix="fa"), popup='<i>Veitch Physiotherapy and Wellness Centre</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.947592994488005, -57.92896400629496], icon = folium.Icon(color="lightblue", icon="fa-bed", prefix="fa"), popup='<i>West Coast Physiotherapy Clinic</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.951044476113324, -57.94003842903224], icon = folium.Icon(color="lightblued", icon="fa-bed", prefix="fa"), popup='<i>Physical Rehab Inc</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.963771766085124, -57.92844481793838], icon = folium.Icon(color="lightblue", icon="fa-bed", prefix="fa"), popup='<i>MOCEAN Physiotherapy and Wellness</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.93997834470666, -57.97686193908858], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Simms Financial Services Limited</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.9428269679589, -57.946448388010936], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Corner Brook Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.552300131611496, -58.570772409504734], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Stephenville Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([47.58939971880313, -59.18378148954363], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Port Aux Basques Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.954982493109064, -54.60675663272965], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Gander Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.953230284312895, -55.635229246823236], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Grand Falls-Windsor Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([49.11993184530017, -55.333973202478255], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Lewisporte Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([48.963771766085124, -57.92844481793838], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills St. Albans Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            #folium.Marker([48.963771766085124, -57.92844481793838], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills Port Saunders Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            folium.Marker([51.419001988704025, -55.70759424448596], icon = folium.Icon(color="red", icon="fa-credit-card", prefix="fa"), popup='<i>Advanced Education And Skills St Anthony Office</i>', tooltip='click me').add_to(map_test).add_to(map_test)
            plugins.Draw().add_to(map_test)
            st_map = st_folium(map_test, width = 850, height = 600, returned_objects=['last_onject_clicked'])
        with right_col:
            with st.expander("See Legend"):
                HtmlFile = open("legend.html", 'r', encoding='utf-8')
                source_code = HtmlFile.read() 
                print(source_code)
                components.html(source_code, height = 765)
