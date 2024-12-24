import PySimpleGUI as sg
from extract_archive_bonus18 import extract_archive

label_zipfile = sg.Text("Select archive: ")
input_zipfile = sg.Input()
button_zipfile = sg.FileBrowse(button_text="Browser...", key="zipfile")

lable_dest = sg.Text("Select folder:")
input_dest = sg.Input()
button_dest = sg.FolderBrowse(button_text="Browser...", key="destfolder")

button_unzip = sg.Button(button_text="Extract", key="unzip")
lable_output = sg.Text(key="output", text_color="green")

window = sg.Window("Extract zip file", layout=[[label_zipfile, input_zipfile, button_zipfile],
                                               [lable_dest, input_dest, button_dest],
                                               [button_unzip, lable_output]])
while True:
    event, value = window.read()
    print(event, value)
    source_file = value["zipfile"]
    dest_folder = value["destfolder"]
    extract_archive(source_file, dest_folder)
    window["output"].update(value="Extract completed!")

window.close()