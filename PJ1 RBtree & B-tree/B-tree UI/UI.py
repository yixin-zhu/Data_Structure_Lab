from tkinter import *
from Btree import *
N = 2

class Gui():
    def __init__(self, window):
        self.myTree = Btree(N)
        self.window = window
        self.window.title("B树操作界面")
        self.window.geometry('1024x676+20+20')
        self.initByFileButton = Button(
            self.window, text="initialize file", width=8, command=self.initialByFile)
        self.deleteButton = Button(
            self.window, text="delete", width=8, command=self.delete)
        self.deleteByFileButton = Button(
            self.window, text="delete file", width=8, command=self.deleteByFile)
        self.insertButton = Button(
            self.window, text="insert", width=8, command=self.insert)
        self.insertByFileButton = Button(
            self.window, text="insert by file", width=8, command=self.insertByFile)
        self.updateButton = Button(
            self.window, text="update", width=8, command=self.update)
        self.searchButton = Button(
            self.window, text="search", width=8, command=self.search)
        self.dumpButton = Button(
            self.window, text="dump", width=8, command=self.dump)
        self.initByFileButton.grid(row=0, column=0)
        self.deleteButton.grid(row=0, column=1)
        self.deleteByFileButton.grid(row=0, column=2)
        self.insertButton.grid(row=0, column=3)
        self.insertByFileButton.grid(row=0, column=4)
        self.updateButton.grid(row=0, column=5)
        self.searchButton.grid(row=0, column=6)
        self.dumpButton.grid(row=0, column=7)
        self.entry1 = Entry(self.window, width=12)
        self.entry2 = Entry(self.window, width=12)
        self.entry3 = Entry(self.window, width=12)
        self.entry1.grid(row=1, column=0)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=1, column=2)
        self.text = Text(self.window, width=120, height=40)
        self.text.grid(row=2, column=0, columnspan=12)

    def initialByFile(self):
        self.myTree = Btree(N)
        src = self.entry1.get()
        if src:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.initialByFile(src))

    def delete(self):
        k = self.entry1.get()
        if k:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.delete(k))

    def deleteByFile(self):
        src = self.entry1.get()
        if src:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.deleteByFile(src))

    def insert(self):
        k = self.entry1.get()
        p = self.entry2.get()
        f = self.entry3.get()
        if(k and p and f):
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.insert(k, p, f))

    def insertByFile(self):
        src = self.entry1.get()
        if src:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.insertByFIle(src))

    def update(self):
        k = self.entry1.get()
        p = self.entry2.get()
        f = self.entry3.get()
        if (k and p and f):
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.update(k, p, f))

    def search(self):
        k = self.entry1.get()
        if k:
            self.text.delete(1.0, END)
            self.text.insert(1.0, self.myTree.search(k))

    def dump(self):
        self.text.delete(1.0, END)
        self.text.insert(1.0, self.myTree.dump())


window = Tk()
root = Gui(window)
window.mainloop()
