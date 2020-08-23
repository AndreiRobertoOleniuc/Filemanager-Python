if modul == "411":
    if doktype == "ocx":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\411\Word")
    elif doktype == "zip":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\411\Programms")
    else:
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\411")
elif modul == "122":
    if doktype == "ocx":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\122\Word")
    elif doktype == "pdf":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\122\Pdf")
    else:
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\122")
elif modul == "153":
    if doktype == "ptx":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\153\PPP")
    elif doktype == "ocx":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\153\Word")
    elif doktype == "sql":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\153\Sql")
    elif doktype == "lsx":
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\153\Excel")
    else:
        shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\153")




import os
import shutil
import glob
import time

a = True
print(os.path.basename(r"C:\Users\Andrei Oleniuc\Downloads"))
while a:
    time.sleep(10)
    os.chdir(r"C:\Users\Andrei Oleniuc\Downloads")
    '''
        Check if a Directory is empty : Method 1
    '''
    if len(os.listdir(r"C:\Users\Andrei Oleniuc\Downloads")) == 0:
        continue
    else:
        def moveAllFilesinDir(srcDir, dstdir):
            if os.path.isdir(srcDir) and os.path.isdir(dstdir):
                for filePath in glob.glob(srcDir + '\*'):
                    filename = str(glob.glob(srcDir + "\*"))
                    if len(filename) > 53:
                        print(filename)
                        '''
                        file = filename[53:]
                        print(file)
                        print(file[43] + file[44] + file[45])
                        size = len(file)
                        modul = file[43] + file[44] + file[45]
                        doktype = file[-5] + file[-4] + file[size - 3]
                        print(size)
                        print(modul)
                        print(doktype)
                        '''
                    '''
                    print(type(filename))
                    print(filename)
                    print(filename[43] + filename[44] + filename[45])
                    print(len(filename))
                    size = len(filename)
                    doktype = filename[-5] + filename[-4] + filename[size - 3]
                    # Fix Tmp problem
                    print(filename[-5] + filename[-4] + filename[size - 3])
                    modul = filename[43] + filename[44] + filename[45]
                    '''
            else:
                print("srcDir & dstDir should be Directories")


        sourceDir = r"C:\Users\Andrei Oleniuc\Downloads"
        destDir = r"C:\Users\Andrei Oleniuc\Desktop"
        moveAllFilesinDir(sourceDir, destDir)
