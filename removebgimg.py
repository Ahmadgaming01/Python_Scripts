from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog


root = Tk()
root.title("Image Viewer")
root.iconbitmap('D:\python Scripts\images.png')

root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select File", filetypes=(("png file" , "*.png"),("all files","*.*")))
my_label = Label(root , text=root.filename).pack()
my_image = ImageTk.PhotoImage(Image.open(root.filename))
my_image_label = Label(image=my_image).pack()
root.mainloop()
