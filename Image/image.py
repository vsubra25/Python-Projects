import sys
import os
from PIL import Image



try:
#grab first and second parameter
    print(sys.argv[1])
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    fileName=""
   

    if(arg1.lower() == ("pokedex/")):
        if(arg2.endswith("/")):
            fileName=arg2
        else:
            print("enter a folder name followed by /")
    else:
        print("please enter the pokedex/")


#check is new/ exists, if not create one        
    if not os.path.exists(fileName):
         os.mkdir(fileName)
#loop through pokedex
#convert img.jpg to .png
#save to new/
    for infile in os.listdir('./pokedex/'):
        f,e=os.path.splitext(infile)
        outfile= f + ".png"
        if infile != outfile:   
         try:
            img= Image.open(arg1+ infile)
            img.save(arg2+outfile)
         except OSError:
            print("cannot convert", infile)
                   
    
except OSError as err:
    print("directory already exists"+ err)


