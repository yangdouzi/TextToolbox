from tkinter import *
# import jieba as jb

root = Tk()
root.title("Text Toolbox")
root.geometry("300x300")
root.resizable(1, 1)
root.configure(bg="lightgreen")
root.iconbitmap("icon.ico")

def jiema():
    root2 = Tk()
    root2.title("Text Toolbox - 解码")
    root2.geometry("300x300")
    root2.resizable(1, 1)
    root2.configure(bg="lightgreen")

    def jiema_go():
        root3 = Tk()
        root3.title("Text Toolbox - 解码结果")
        root3.geometry("300x300")
        root3.resizable(1, 1)
        root3.configure(bg="lightgreen")

        ntext = ""
        for i in text.get():
            print(ord(i))
            ntext += chr(ord(i)-5)

        Label(root3, text=ntext, font=("Microsoft Yahei", 12)).pack(pady=20)

    text = Entry(root2, width=100, font=("Microsoft Yahei", 12))
    text.pack(pady=20)
    text.insert(0, "请输入文本")

    ok = Button(root2, text="解码", command=jiema_go)
    ok.pack(pady=20)

def jiami():
    root2 = Tk()
    root2.title("Text Toolbox -加密")
    root2.geometry("300x300")
    root2.resizable(1, 1)
    root2.configure(bg="lightgreen")

    def jiema_go():
        root3 = Tk()
        root3.title("Text Toolbox - 加密结果")
        root3.geometry("300x300")
        root3.resizable(1, 1)
        root3.configure(bg="lightgreen")

        ntext = ""
        for i in text.get():
            print(ord(i))
            ntext += chr(ord(i)+5)

        Label(root3, text=ntext, font=("Microsoft Yahei", 12)).pack(pady=20)

    text = Entry(root2, width=100, font=("Microsoft Yahei", 12))
    text.pack(pady=20)
    text.insert(0, "请输入文本")

    ok = Button(root2, text="加密", command=jiema_go)
    ok.pack(pady=20)

b1 = Button(root, text="解码", command=jiema)
b1.pack(pady=20)
b2 = Button(root, text="加密", command=jiami)
b2.pack(pady=20)

mainloop()