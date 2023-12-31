from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube,Playlist
import os


#functionality part
def download():
    got_path=filedialog.askdirectory()
    link_url=text.get()
    print(link_url)

    yt=YouTube(link_url)
    yt.streams.get_highest_resolution().download(got_path)
    messagebox.showinfo('success''downloading is success')
    os.startfile(got_path)


root = Tk()
root.title("vk video downloader")
root.config(bg='red4')
outerframe = Frame(root)
outerframe.grid(row=0, column=0, pady=30, padx=30)
logoImage = PhotoImage(file='logo.png')
logolabel = Label(outerframe, image=logoImage)
logolabel.grid(row=0, column=0)

innerframe = LabelFrame(outerframe, text='DOWNLOAD', font=('arial black', 14, 'bold'))
innerframe.grid(row=1, column=0, pady=20)
radioImage = PhotoImage(file='video.png')
videoradioButton = Radiobutton(innerframe, image=radioImage, text='HD video', compound=LEFT, relief='solid')
videoradioButton.grid(row=0, column=0, padx=20)

playlistImage = PhotoImage(file='shuffle.png')
playlistradioButton = Radiobutton(innerframe, image=playlistImage, text='playlist', compound=LEFT, relief='solid')
playlistradioButton.grid(row=0, column=2, padx=20)

text = StringVar()
url_entryField = Entry(outerframe, width=60, font=('arial', 14, 'bold'), justify=CENTER, textvariable=text, fg='gray')
url_entryField.grid(row=2, column=0, padx=10, pady=30)
text.set('Enter URL')


def click(event):
    url_entryField.delete(0, END)
    url_entryField.config(fg='black')


url_entryField.bind('<Button-1>', click)

downloadImage = PhotoImage(file='download.png')
downloadButton = Button(outerframe, image=downloadImage,command=download)
downloadButton.grid(row=3, column=0, pady=30)

root.mainloop()
