import folium
import streamlit as st
import pandas as pd
import re


from streamlit_folium import st_folium 


df = pd.read_excel('tech teams project\CombinedSheetCleanedv3.xlsx', dtype=str)
#df.reset_index(inplace=True)
#df['OPENING_HRS'] = pd.to_datetime(df['OPENING_HRS']).dt.date

def format_phone_number(phone_number):
    phone_number = re.sub('[^0-9]+', '', phone_number)
    return '(' + phone_number[:3] + ') ' + phone_number[3:6] + '-' + phone_number[6:]

folium.IFrame()

m = folium.Map(location=[48.94755283613525, -57.96092308785148], zoom_start=16)

for row in df.itertuples(index=False,name=None):
    if pd.isna(row[13]) == True:
        continue
    else:


        folium.Marker([row[13], row[14]], popup=folium.Popup(f"""<font size='2.5'>
                                                                {f'<img src="{row[17]}" width="350" height="250"><br>' if pd.isnull(row[17]) is not True and row[17] != 'no image' else ''}

                                                                <strong>Name:</strong> {row[0].title()}<br>
                                                                <strong>Service/Support: </strong>{row[1].title()}<br>
                                                                <strong>Address: </strong>{f'{str(row[2]).split(",", 1)[0]}, ' if pd.isnull(row[2]) is not True else ''}{row[3]} {str(row[4]).split(' and', 1)[0]} {row[5]}<br>
                                                                <strong>Region: </strong> {row[6]}<br>
                                                                {f'<strong>Opening Hours: </strong> {str(row[7])}<br>' if pd.isnull(row[7]) is not True else ''}
                                                                {f'<strong>Closing Hours: </strong> {row[8]}<br>' if pd.isnull(row[8]) is not True else ''}
                                                                {f'<strong>Telephone: </strong> {format_phone_number(row[9])}<br>' if pd.isnull(row[9]) is not True else ''}


                                                                
                                                                </font>
                                                                """, max_width=1000),
 tooltip=f'{row[0].title()}').add_to(m)
        print(pd.isnull(row[8]))
        
st.write(df)
    
st_data = st_folium(m, width=725)