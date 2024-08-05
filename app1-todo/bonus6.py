import PySimpleGUI as Sg

label1 = Sg.Text("Enter feet:")
input1 = Sg.Input()

label2 = Sg.Text("Enter Inches:")
input2 = Sg.Input()


convert_button = Sg.Button("convert")
window = Sg.Window("Convertor", layout = [[label1 , input1], [label2, input2],[convert_button] ])


window.read()
window.close()