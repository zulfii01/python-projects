from pytube import YouTube
from tkinter import *

a = Tk()
a.geometry("700x700")
a.config(bg="black")
a.title("Video Downloader")

Label(a, text="Youtube", font=("Arial", 29, "bold"), bg="light pink").pack()
Label(a, text="Video Downloader", font=("Arial", 29, "bold"), bg="light pink").pack()

link = StringVar()
Label(a, text="Enter the link", font=("Arial", 24, "bold")).place(x=240, y=200)

Entry(a, width=49, font=31, textvariable=link, bd=1).place(x=80, y=250)


def fun1():
    url = YouTube(str(link.get()))
    v = url.streams.first()
    v.download()

    Label(a, text="Downloading Completed!!", font=("Arial", 26, "bold"), bg="yellow").place(x=150, y=400)
    Label(a, text="Check the respective folder", font=("Arial", 26, "bold"), bg="yellow").place(x=150, y=550)


Button(a, text="Download", font=("Arial", 26, "bold"), bg="light green", command=fun1).place(x=240, y=300)
a.mainloop()
