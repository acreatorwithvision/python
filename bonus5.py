import PySimpleGUI as Sg

label1 = Sg.Text("Select Files to compress: ")
input1 = Sg.Input()
choose_button1 = Sg.FilesBrowse("Choose")

label2 = Sg.Text("Select Destination: ")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose")

window=Sg.Window("File compressor", layout=[[label1, input1, choose_button1 ],
                                            [label2, input2, choose_button2]])

window.read()
window.close()



 