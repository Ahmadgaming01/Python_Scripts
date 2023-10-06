import os
import shutil


datei_pfad = input("Geben Sie der Pfad : ") 

pfad = os.path.dirname(os.path.join( datei_pfad ))


for pfadname in os.listdir(pfad):
    print(pfadname)