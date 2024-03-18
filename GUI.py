import functions #import functions.py file 
import PySimpleGUI as sg#GUI module in python which needs to be downloaded before working on that.


label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
print("hello")
window.close()



