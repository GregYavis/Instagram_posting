import config
import instabot
import tkinter as tk
from tkinter import Label
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
from instabot import bot

USER = config.USER_LOGIN
PASSWD = config.USER_PASSWD
bot = instabot.Bot()


class Select:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        selectButton = tk.Button(self.master, text='Select image', fg='black',
                                 width=40, command=self.selectImage)
        selectButton.pack()
        self.frame.pack()

    def selectImage(self):
        self.master.destroy()
        self.master = tk.Tk()
        self.Select_path = askopenfilename(initialdir="/home/yavis/Pictures")
        # self.todemo = DEMO(Select_path)
        self.app = Post(self.master, self.Select_path)
        self.master.mainloop()


class Post(Select):
    def __init__(self, master, Select_path):
        global fileToPost
        self.master = master
        self.img = Image.open(Select_path)
        self.width = self.img.size
        self.ratio = int(self.width[0]) // 300
        self.img_resized = self.img.resize((self.img.width // self.ratio,
                                            self.img.height // self.ratio))
        self.weight, self.highth = str(self.img_resized).split()[3].split('=')[
            1].split('x')
        self.geometry = str(str(int(self.weight)*2-100) + 'x' + str(int(
            self.highth)*2+100))

        self.master.geometry(self.geometry)
        fileToPost = Select_path
        self.button = tk.Button(self.master, text='Post photo to '
                                                  'Instagramm', command
                                =self.upload)
        self.button.pack()

        self.labe = Label(text='Enter text')
        self.labe.pack()
        self.cap = tk.Text(self.master, width=40, height=10)
        self.cap.pack()


        self.tkimage = ImageTk.PhotoImage(self.img_resized)
        self.myvar = Label(self.master, image=self.tkimage)
        self.myvar.image = self.tkimage
        self.myvar.pack()

    def upload(self):
        bot.login(username=USER, password=PASSWD)
        CaptionToPost = self.cap.get('1.0', 'end-1c')
        bot.upload_photo(fileToPost, caption=CaptionToPost)


def main():
    root = tk.Tk()
    root.title('PostBot.V 0.5')
    Select(root)
    root.mainloop()


if __name__ == '__main__':
    main()
