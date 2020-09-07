import os
import shutil
import glob
import time


def main():
    moveItems()


def moveItems():
    ###################################################
    # Program Logic
    a = True
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
                    try:
                        for filePath in glob.glob(srcDir + '\*'):
                            filename = str(glob.glob(srcDir + "\*"))
                            print("Dies sind die Files welche in Download sind: " + "\n" + filename)
                            print()
                            print("Modul: " + filename[43] + filename[44] + filename[45] + "\n" +
                                  "Falls das die Zahl nicht dreistellig ist oder aus Buchstaben \n" +
                                  "besteht hat dieses File kein genanntes Modul")
                            print()
                            size = len(filename)
                            doktype = filename[-5] + filename[-4] + filename[size - 3]
                            # Fix Tmp problem
                            print("Dies ist der Datein Typ: "+filename[-5] + filename[-4] + filename[size - 3])
                            modul = filename[43] + filename[44] + filename[45]

                            if modul == "133":
                                if doktype == "ocx":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Word")
                                elif doktype == "zip":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Programme")
                                elif doktype == "ptx":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\PPP")
                                elif doktype == "lsx":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Excel")
                                elif doktype == "pdf":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Pdf")
                                else:
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133")
                            else:
                                if doktype == "ptx":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\PPP")
                                elif doktype == "lsx":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Excel")
                                elif doktype == "tmp":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\Bin")
                                elif doktype == "pdf":
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\BBB\133\Pdf")
                                else:
                                    shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop")
                            print()
                            print("Das File wurde Erfolgreich in das zugewissene Verzeichnis verschoben")
                    except OSError as e:
                        print(e.errno)
                        for filePath in glob.glob(srcDir + '\*'):
                            shutil.move(filePath, r"C:\Users\Andrei Oleniuc\Desktop\Schule\Bin")
                else:
                    print("srcDir & dstDir should be Directories")

            sourceDir = r"C:\Users\Andrei Oleniuc\Downloads"
            destDir = r"C:\Users\Andrei Oleniuc\Desktop"
            moveAllFilesinDir(sourceDir, destDir)


if __name__ == '__main__':
    main()
