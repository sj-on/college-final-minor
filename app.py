from fileinput import filename
import tkinter as tk
from tkinter import filedialog

from unmain import extract

filename = None

def browseFiles():
	global filename
	filename = filedialog.askopenfilename(initialdir = "./", title = "select a file", filetypes = (("jpeg files","*.jpg*"),("png files","*.png*")))
	file_details.configure(text="file selected: " + filename)

def evaluate_colour(event):
	total_colours = int(num_of_c.get())
	if filename is not None:
		extract(filename, total_colours)

window = tk.Tk()
window.title("colour extractor")
window.columnconfigure([0, 1, 2], minsize=50)
window.rowconfigure([0, 1, 2], minsize=30)

greeting = tk.Label(window, text="n-dominant colours extractor")
browse_button = tk.Button(window, text="browse file", command=browseFiles)
file_details = tk.Label(window, text='')
num_of_c = tk.Entry(window)
num_of_c.bind("<Return>", evaluate_colour)

greeting.grid(row=1, column=0, pady=8, padx=8)
browse_button.grid(row=1, column=2)
file_details.grid(row=2, column=0, pady=8, padx=8)
num_of_c.grid(row=2, column=2, pady=8, padx=8)

window.mainloop()