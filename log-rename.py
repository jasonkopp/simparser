import os, shutil

scriptfolder = "/Users/jasonkopp/Documents/SimCloud/Results_Log/5-Tango/HEVC/"

for qpfolder in os.listdir(scriptfolder):
    if os.path.isdir(scriptfolder + qpfolder + "/"):
        for file in os.listdir(scriptfolder + qpfolder + "/"):
            if file == 'console1':
                print       (scriptfolder + qpfolder + "/console1", scriptfolder + qpfolder + ".log")
                os.rename   (scriptfolder + qpfolder + "/console1", scriptfolder + qpfolder + ".log")
        shutil.rmtree(scriptfolder+qpfolder + "/")
