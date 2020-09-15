from PIL import ImageTk,Image
import subprocess
import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_writer = PdfFileWriter()
root = tkinter.Tk()
root.focus_force()
root.title("PDF-Merge")
root.iconbitmap(default='assets/Icon.ico')


ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (600/2)
y = (hs/2) - (500/2)
root.geometry('%dx%d+%d+%d' % (600, 500, x, y))


def fileopen():
    global files
    files = filedialog.askopenfilenames(parent=root,title = "PDF-File Selector",filetypes=[("PDF files","*.pdf")])
    if files == "":
        return
    roundedbutton["command"] = merge
    loadimage1 = tkinter.PhotoImage(file="assets/MergeButton.png")
    roundedbutton["image"] = loadimage1
    root.mainloop()
    return


def merge():
    saveas = filedialog.asksaveasfilename(defaultextension = ".pdf")
    if saveas == "":
        return
    for file in root.tk.splitlist(files):
        pdf_reader = PdfFileReader(file)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(saveas,"wb") as out:
        pdf_writer.write(out)
    root.destroy()
    subprocess.Popen([saveas],shell=True)


canvas = tkinter.Canvas(root, width = 600, height = 500)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("assets/MainPage.png"))
canvas.create_image(0, 0, anchor="nw", image=img)


loadimage = tkinter.PhotoImage(file="assets/Button.png")
roundedbutton = tkinter.Button(root,anchor ="nw", image=loadimage,command= fileopen)
button1Window = canvas.create_window(212,325,anchor = "nw",window = roundedbutton)

roundedbutton["bg"] = "#313742"
roundedbutton["border"] = "0"
roundedbutton["activebackground"] = "#313742"


root.mainloop()
