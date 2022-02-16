#!/usr/bin/env python3

import tkinter
import platform


class Marquee:
    def __init__(self, root, marquee_str):
        self.root = root
        # 设置窗口置顶
        self.root.attributes('-topmost', True)
        # 设置窗口全屏
        self.root.attributes('-fullscreen', True)
        # 设置窗口背景透明（Windows：指定一种颜色作为透明色， Mac：设置内容透明）
        if platform.system() == 'Windows':
            self.root.attributes('-transparentcolor', 'black')
        elif platform.system() == 'Darwin':
            self.root.attributes('-transparent', True)

        # 创建一个tk的String变量，用于绑定控件后，实现动态修改控件显示内容
        self.str_var = tkinter.StringVar(value=marquee_str)

        # 创建Label标签，用于显示文字内容
        self.label = tkinter.Label(self.root)
        # 将标签的内容和str_var绑定，当str_var被修改时，标签的内容就会跟着改变
        self.label['textvariable'] = self.str_var
        # 设置窗口背景透明（Windows：将背景色设置为前面指定的透明色， Mac：设置背景色为透明）
        if platform.system() == 'Windows':
            self.label['bg'] = 'black'
        elif platform.system() == 'Darwin':
            self.label['bg'] = 'systemTransparent'
        # 设置标签文字颜色
        self.label['fg'] = '#d6604e'
        # 设置标签文字字体
        self.label['font'] = ('TkHeadingFont', 75, 'bold')
        # 将创建的标签定位到窗体上（执行了pack标签才会显示），并设置标签平铺整个窗口
        self.label.pack(fill='both', expand=True)

        # marquee文字刷新间隔（ms）
        self.interval = 150
        # 利用tk的after机制刷新标签
        self.root.after(self.interval, self.change_str)

        # 运行窗口
        self.root.mainloop()

    def change_str(self):
        """改变marquee文字显示内容"""
        tmp = self.str_var.get()
        self.str_var.set(tmp[1:] + tmp[0])
        # 循环调用change_str，实现循环滚动效果
        self.root.after(self.interval, self.change_str)


if __name__ == '__main__':
    Marquee(tkinter.Tk(), '阿梨今天开胯了吗...   ')
