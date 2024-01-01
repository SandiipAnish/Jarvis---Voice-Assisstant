import subprocess
import datetime

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    fh = open("Note.txt", 'a+')
    fh.write(text+'\n \n')
    fh.close()

