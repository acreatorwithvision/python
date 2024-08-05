import PySimpleGUI as Sg
from zip_creator import make_archive

label1 = Sg.Text("Select Files to compress: ")
input1 = Sg.Input()
choose_button1 = Sg.FilesBrowse("Choose", key="files")

label2 = Sg.Text("Select Destination for files: ")
input2 = Sg.Input()
choose_button2 = Sg.FolderBrowse("Choose", key="folder")

compress_button=Sg.Button("Compress")

label3=Sg.Text(key="output",text_color="Green")

window=Sg.Window("File compressor", layout=[[label1, input1, choose_button1 ],
                                            [label2, input2, choose_button2],[compress_button, label3]])


while True:
    event, values=window.read()
    print(event, values)
    filepaths=values["files"].split(";")#list of files that are being selected as input.
    folder=values["folder"]#output folder in the form of list
    make_archive(filepaths,folder)
    window["output"].update(value="compression completed")




window.close()



 