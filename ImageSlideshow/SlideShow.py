from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk


root = tk.Tk()
root.title("Image Slideshow Viewer")

#List of Image Path
image_paths = [

    r"C:\Users\LENOVO\OneDrive\Pictures\m5.jpg",
    r"C:\Users\LENOVO\OneDrive\Pictures\m4.png",
    r"C:\Users\LENOVO\OneDrive\Pictures\m3.jpg",
    r"C:\Users\LENOVO\OneDrive\Pictures\m2.jpg",
    r"C:\Users\LENOVO\OneDrive\Pictures\fit.jpg"

]
#Resize the image to 1080x1080 size
image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root,text= 'Play slideshow' , command=start_slideshow)
play_button.pack()

root.mainloop()