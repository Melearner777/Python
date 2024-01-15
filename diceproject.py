#importing modules
import tkinter as tk
from PIL import Image, ImageTk
import random

#Creating the Tkinter Window
window = tk.Tk()
window.geometry("500x360")
window.title("Dice rolling simulator")

#Loading Dice Images
dice = ["dice1.png.png", "dice2.png.png", "dice3.png.png", "dice4.png.png", "dice5.png.png", "dice6.png.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))


#Creating Labels for Dice Images
label1 = tk.Label(window,image=image1)
label1.image = image1
label1.place(x = 200, y = 150)

#Defining the dice_roll Function:
def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image=image1

#Creating the Roll Button:
button = tk.Button(window,text="ROLL",bg = "black", fg = "white",font= "Times 20 bold",command=dice_roll)
button.place(x = 200, y = 0)

#Running the Tkinter Event Loop
window.mainloop()