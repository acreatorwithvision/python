import zipfile
import pathlib



def make_archive(filepaths, dest_dir): #directory cannot be given directly. Its path should be given instead.
    dest_path=pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath=pathlib.Path(filepath)
            archive.write(filepath,filepath.name)
        


if __name__ == "__main__":
    make_archive(filepaths=["bonus.py","bonus2.py"],dest_dir="dest")

    #what we did here is we created a function called make_archive() that will take
    #two parameters filepaths and dest_dir. filepaths is the path to the file selected and dest_dir is the path to the destination.
    #filepaths can be given as files but dest_dir cannot be given as directory name, instead a path of the 
    #compressedfile should be added next to the name of the directory.