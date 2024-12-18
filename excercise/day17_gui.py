import PySimpleGUI as sg
from day17_function import convert

label_feet = sg.Text("Enter feet: ")
input_feed = sg.Input(key="feet")

label_inch = sg.Text("Enter inchs: ")
input_inch = sg.Input(key="inch")

button_convert = sg.Button(button_text="Convert", key="convert")
output_meter = sg.Text(key="meter")

window = sg.Window(title="Covertor", layout=[[label_feet, input_feed],
                                             [label_inch, input_inch],
                                             [button_convert, output_meter]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inch = float(values["inch"])
    meter = convert(feet, inch)
    window["meter"].update(value=meter)

window.close()
