import PySimpleGUI as sg 
import pandas as pd

sg.theme("DarkBlue13")

EXCEL_FILE = "H&S_ServiceProviders.xlsx"
 
df = pd.read_excel(EXCEL_FILE)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key="NAME")],
    [sg.Text("Service/Support", size=(15,1)), sg.Combo(["Financial aid", "Community dietican", "Food subsidies", "Social Worker", "In/outpatient rehabilitation", 
                                                        "Psychologist/Psychiatrist", "Speech Language Pathologist", "Occupational Therapist", "Physiotherapist",
                                                        "Peer support group", "Skilled nursing facilities", "Home-based rehabilitation", "Pharmacist", "Kinesiologist"
                                                        "Sexologist"], key="SERVICE/SUPPORT")],   
    [sg.Text("Address", size=(15,1)), sg.InputText(key="ADDRESS")],
    [sg.Text("Community", size=(15,1)), sg.InputText(key="COMMUNITY")],
    [sg.Text("Province", size=(15,1)), sg.Combo(["Newfoundland", "Labrador"], key="PROVINCE")],
    [sg.Text("Postal Code", size=(15, 1)), sg.InputText(key="POSTAL_CODE")],
    [sg.Text("Region:", size=(15,1)),
                            sg.Checkbox("Western", key="REGION"),
                            sg.Checkbox("Central", key="REGION"),
                            sg.Checkbox("Eastern", key="REGION"),
                            sg.Checkbox("Labrador-Grenfell", key="REGION")],
    [sg.Text("Opening Hours", size=(15,1)), sg.InputText(key="OPENING_HRS")],
    [sg.Text("Closing Hours", size=(15,1)), sg.InputText(key="CLOSING_HRS")],
    [sg.Text("Telephone", size=(15,1)), sg.InputText(key="TELEPHONE")],
    [sg.Text("Additional Telephone", size=(15,1)), sg.InputText(key="ADD_PHONE")],
    [sg.Text("Email", size=(15,1)), sg.InputText(key="EMAIL")],
    [sg.Text("Website", size=(15,1)), sg.InputText(key="WEBSITE")],
    [sg.Text("Information", size=(15,1)), sg.InputText(key="INFO")],
    [sg.Text("Source", size=(15,1)), sg.InputText(key="SOURCE")],
    [sg.Text("Image (URL Link)", size=(15,1)), sg.InputText(key="IMG")],  
    [sg.Text("-" * 150)],
    [sg.Text("Choose A Folder", size=(30, 1))],
    [sg.Text("Folder", size=(15,1), auto_size_text=False, justification="right"),
        sg.InputText("Default Folder"), sg.FolderBrowse()],
    [sg.Submit(), sg.Button("Clear"), sg.Exit()]

]

window = sg.Window("Heart & Stroke Resources", layout)

def clear_input():
    for key in values:
        window[key].update("")
    return None

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Clear":
        clear_input()
    if event == "Submit":
        ## creates new row in df with input values 
        new_data = pd.DataFrame([values], columns=df.columns)
        ## Concatenate the new row with the existing df
        df = pd.concat([df, new_data], ignore_index=True)
        ##Save the updated df to the Excel Sheet
        df.to_excel(EXCEL_FILE, index=False)
        ## Show popup msg confirming the entry is completed 
        sg.popup("Data Entry Complete")
        ## Clear input values so new values can be inputed
        clear_input()
window.close()
