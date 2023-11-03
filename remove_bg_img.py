from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog


root = Tk()
root.title("Image Viewer")
root.iconbitmap ('C:\Users\almad\Desktop')

def open():
    global img_path
    img_path=filedialog.askopenfilename(initialdir="C:/", title="Select File",)
    