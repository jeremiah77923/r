from tkinter import *

window = Tk()
window.config(bg="red")
window.title("Mile to Km Converter")
window.minsize(width=100, height=75)

input = Entry(width=5)
input.grid(row=35, column=200)

label = Label(text="Miles")
label.grid(row=35, column=220)
label.config(bg="red")

label1 = Label(text="is equal to")
label1.grid(row=50, column=180)
label1.config(bg="red")

label2 = Label(text=" ")
label2.grid(row=50, column=200)
label2.config(bg="red")

label3 = Label(text="Km")
label3.grid(row=50, column=220)
label3.config(bg="red")


def button_clicked():
    km = int(input.get())
    km *= 1.609
    label2.config(text=km)


button = Button(text="Calculate", command=button_clicked, bg="black")
button.grid(row=70, column=200)
button.config(bg="blue")

window.mainloop()
