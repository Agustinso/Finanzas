#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter.font import Font


class LogFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.list_box = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.list_box.configure(font=Font(family="Lato Light", size=12))
        for line in range(100):
            self.list_box.insert(END, "This is line number " + str(line))
            self.list_box.pack(side=LEFT, fill=BOTH)
        self.list_box.itemconfig(1, {'bg': 'red'})
        self.scrollbar.config(command=self.list_box.yview)


class SummaryFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.list_box = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.list_box.configure(font=Font(family="Lato Light", size=12))
        for line in range(100):
            self.list_box.insert(END, "This is line number " + str(line))
            self.list_box.pack(side=LEFT, fill=BOTH)
        self.list_box.itemconfig(1, {'bg': 'red'})
        self.scrollbar.config(command=self.list_box.yview)


class App(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title('Finanzas')
        self.notebook = ttk.Notebook(self)
        self.log_frame = LogFrame()
        self.summary_frame = SummaryFrame()
        self.notebook.add(self.log_frame, text="Log")
        self.notebook.add(self.summary_frame, text="Summary")
        self.notebook.pack(padx=0, pady=0)
        self.pack()


def main():
    main_window = Tk()
    app = App(main_window)
    app.mainloop()
    return 0


if __name__ == '__main__':

    main()
