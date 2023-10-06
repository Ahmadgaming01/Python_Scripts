import os
import shutil


datei_pfad = input("Geben Sie der Pfad : ") 

#pfad = os.path.dirname(os.path.join( datei_pfad ))


for pfadname in os.listdir(datei_pfad):
    

    if pfadname.endswith(('.png' , '.jpg','.gif','.jpeg')):
        if not os.path.exists('Applications'):
            os.mkdir('images')
        shutil.copy(pfadname , 'images')
        os.remove(pfadname)
        print('Fertig erstellt')

    if pfadname.endswith(('.exe' )):
        if not os.path.exists('Applications'):
            os.mkdir('Applications')
        shutil.copy(pfadname , 'Applications')
        os.remove(pfadname)
        print('Fertig erstellt')

