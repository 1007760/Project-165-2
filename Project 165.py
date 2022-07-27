from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.geometry("500x500")
root.title("Project 164-165")
root.configure(bg = "teal")
image = Label(root, bg = "teal")
image.place(relx = 0.5, rely = 0.5, anchor = CENTER)
img_path = ""

def openimage() :
    global img_path
    img_path = filedialog.askopenfilename(title = "Open image file", filetypes = [("Image Files","*.jpg;*.gif;*.jpg;;*.png;*.txt")])
    print(img_path)
    img1 = Image.open(img_path)
    load_img = ImageTk.PhotoImage(img1)
    image["image"] = load_img
    load_img.close()
    
def rotateImage() :
    global img_path
    img1 = Image.open(img_path)
    rotated_img = img1.rotate(90)
    load_img = ImageTk.PhotoImage(rotated_img)
    load_img.close()

open_btn = Button(root, text = "Open Image", bg = "teal", command = openimage)
open_btn.place(relx = 0.5, rely = 0.3, anchor = CENTER)
rotate_btn = Button(root, text = "Rotate Image", bg = "teal", font = ("MS Gothic", 12), command = rotateImage, relief = SOLID, padx = 15, pady = 10)
rotate_btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)
root.mainloop()