#!/usr/bin/env python3

import tkinter


class Marquee:
    def __init__(self, root, marquee_str):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-transparentcolor', 'black')

        self.str_var = tkinter.StringVar(value=marquee_str)

        self.label = tkinter.Label(self.root)
        self.label['textvariable'] = self.str_var
        self.label['bg'] = 'black'
        self.label['fg'] = '#d6604e'
        self.label['font'] = ('TkHeadingFont', 75, 'bold')
        self.label.pack(fill='both', expand=True)

        self.interval = 150
        self.root.after(self.interval, self.change_str)

        self.root.mainloop()

    def change_str(self):
        self.root.lift()
        tmp = self.str_var.get()
        self.str_var.set(tmp[1:] + tmp[0])
        self.root.after(self.interval, self.change_str)


if __name__ == '__main__':
    Marquee(tkinter.Tk(), '阿梨今天开胯了吗...   ')
